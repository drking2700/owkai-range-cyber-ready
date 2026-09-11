from __future__ import annotations
import json, re
from .missions import load_manifest
from .models import AARSubmission
from .costs import estimate_tokens, estimate_cost, enforce_budget, record_usage
from .db import connect, now

DIMENSIONS = ["accuracy", "risk_reasoning", "fix_justification", "verification", "communication"]

def questions(mission_id: int) -> list[dict]:
    m = load_manifest(mission_id)
    return [
        {"id":"what", "prompt":f"What was the security problem in {m['title']} and what evidence proved it?"},
        {"id":"risk", "prompt":"What could happen if the issue remained unresolved? Explain the risk, not just the technical defect."},
        {"id":"fix", "prompt":"What did you change, and why was that correction proportionate?"},
        {"id":"verify", "prompt":"How did you verify the result independently of AI output?"},
        {"id":"ai", "prompt":"Where did AI help, where was it incomplete or wrong, and what remained your responsibility?"},
        {"id":"communicate", "prompt":"Explain the result in two or three sentences to a nontechnical manager."},
    ]

def _score_answer(text: str, dimension: str) -> int:
    t = text.strip()
    if not t: return 0
    score = 1
    if len(t) >= 60: score += 1
    if len(t) >= 140: score += 1
    evidence_terms = {
      "accuracy": ["evidence", "file", "config", "observed", "verified"],
      "risk_reasoning": ["risk", "impact", "attacker", "exposure", "business"],
      "fix_justification": ["because", "least", "limit", "control", "changed"],
      "verification": ["test", "verify", "hash", "assert", "passed", "evidence"],
      "communication": ["risk", "impact", "recommend", "business", "because"],
    }
    if any(k in t.lower() for k in evidence_terms[dimension]): score += 1
    if dimension == "verification" and ("ai said" in t.lower()) and not any(k in t.lower() for k in ["test","verify","evidence","file","hash","assert"]):
        score = min(score, 2)
    return min(score, 5)

def score(sub: AARSubmission) -> dict:
    joined = "\n".join(sub.answers.values())
    inp = estimate_tokens(joined + sub.ai_work_record.model_dump_json())
    enforce_budget(sub.learner_id, inp + 300)
    mapping = {
        "accuracy": sub.answers.get("what", ""),
        "risk_reasoning": sub.answers.get("risk", ""),
        "fix_justification": sub.answers.get("fix", ""),
        "verification": sub.answers.get("verify", ""),
        "communication": sub.answers.get("communicate", ""),
    }
    scores = {d: _score_answer(mapping[d], d) for d in DIMENSIONS}
    ai_answer = sub.answers.get("ai", "").lower()
    if not any(k in ai_answer for k in ["verify", "wrong", "incomplete", "evidence", "responsib"]):
        scores["verification"] = max(0, scores["verification"] - 1)
    avg = round(sum(scores.values()) / len(scores), 2)
    feedback = (
        "AAR complete. Preserve the strongest objective evidence in the learner repository. "
        + ("Reasoning is developing; review any dimension below 3 before advancing." if avg < 3 else "The explanation shows a defensible link between finding, risk, correction, and verification.")
    )
    out = estimate_tokens(feedback + json.dumps(scores))
    cost = estimate_cost(inp, out)
    record_usage(sub.learner_id, sub.mission_id, "aar", inp, out, cost)
    with connect() as con:
        con.execute(
            "INSERT INTO aar_records(learner_id, mission_id, transcript_json, scores_json, created_at) VALUES (?,?,?,?,?)",
            (sub.learner_id, sub.mission_id, json.dumps(sub.answers), json.dumps(scores), now()),
        )
        con.execute(
            "INSERT INTO progress(learner_id, mission_id, status, aar_score, updated_at) VALUES (?,?,?,?,?) "
            "ON CONFLICT(learner_id, mission_id) DO UPDATE SET status='aar_complete', aar_score=excluded.aar_score, updated_at=excluded.updated_at",
            (sub.learner_id, sub.mission_id, "aar_complete", avg, now()),
        )
    return {"scores": scores, "total_average": avg, "feedback": feedback, "estimated_cost_usd": cost}
