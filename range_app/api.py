from __future__ import annotations
from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import PlainTextResponse, StreamingResponse
from pathlib import Path
import json, io, zipfile
from .missions import list_missions, load_manifest
from .models import AssistRequest, AARSubmission, ProgressUpdate
from .ai import assist
from .aar import questions, score
from .db import connect, ensure_learner, now
from .portfolio import render_portfolio
from .auth import current_learner

router = APIRouter(prefix="/api")

@router.get("/health")
def health(): return {"status":"ok", "mode":"ai-native-human-accountable"}

@router.get("/missions")
def missions(): return list_missions()


@router.get("/me")
def me(request: Request):
    return {"learner_id": current_learner(request)}

@router.get("/missions/{mission_id}/starter.zip")
def starter_zip(mission_id: int):
    from .missions import mission_dir
    try:
        load_manifest(mission_id)
    except KeyError:
        raise HTTPException(404, "Mission not found")
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as z:
        base = mission_dir(mission_id) / "starter"
        for fp in base.rglob("*"):
            if fp.is_file():
                z.write(fp, fp.relative_to(base))
        template = Path(__file__).resolve().parents[1] / "schemas" / "ai_work_record.template.json"
        z.write(template, "ai_work_record.json")
    buf.seek(0)
    return StreamingResponse(buf, media_type="application/zip", headers={"Content-Disposition": f"attachment; filename=mission-{mission_id:02d}-starter.zip"})

@router.get("/missions/{mission_id}")
def mission(mission_id: int):
    try: return load_manifest(mission_id)
    except KeyError: raise HTTPException(404, "Mission not found")

@router.post("/assist")
def ai_assist(req: AssistRequest):
    ensure_learner(req.learner_id)
    try: return assist(req.learner_id, req.mission_id, req.question)
    except ValueError as e: raise HTTPException(400, str(e))

@router.get("/aar/{mission_id}/questions")
def aar_questions(mission_id: int): return questions(mission_id)

@router.post("/aar/submit")
def aar_submit(sub: AARSubmission):
    ensure_learner(sub.learner_id)
    try: return score(sub)
    except ValueError as e: raise HTTPException(400, str(e))

@router.get("/progress/{learner_id}")
def progress(learner_id: str):
    ensure_learner(learner_id)
    with connect() as con:
        return [dict(r) for r in con.execute("SELECT * FROM progress WHERE learner_id=? ORDER BY mission_id", (learner_id,)).fetchall()]

@router.post("/progress")
def update_progress(u: ProgressUpdate):
    ensure_learner(u.learner_id)
    with connect() as con:
        con.execute(
            "INSERT INTO progress(learner_id,mission_id,status,verifier_passed,aar_score,updated_at) VALUES (?,?,?,?,?,?) "
            "ON CONFLICT(learner_id,mission_id) DO UPDATE SET status=excluded.status, verifier_passed=excluded.verifier_passed, aar_score=COALESCE(excluded.aar_score,progress.aar_score), updated_at=excluded.updated_at",
            (u.learner_id,u.mission_id,u.status,int(u.verifier_passed),u.aar_score,now()),
        )
    return {"ok": True}

@router.get("/review/learners")
def reviewer_learners():
    with connect() as con:
        learners = [dict(r) for r in con.execute("SELECT * FROM learners ORDER BY created_at").fetchall()]
        for l in learners:
            l["progress"] = [dict(r) for r in con.execute("SELECT * FROM progress WHERE learner_id=? ORDER BY mission_id", (l["id"],)).fetchall()]
        return learners

@router.post("/review/{learner_id}/{mission_id}")
def human_review(learner_id: str, mission_id: int, body: dict):
    decision = body.get("decision")
    if decision not in {"approve","changes_requested"}:
        raise HTTPException(400, "decision must be approve or changes_requested")
    reviewer = body.get("reviewer", "reviewer")
    notes = body.get("notes", "")
    with connect() as con:
        con.execute("INSERT INTO human_reviews(learner_id,mission_id,reviewer,decision,notes,created_at) VALUES (?,?,?,?,?,?)", (learner_id,mission_id,reviewer,decision,notes,now()))
        if decision == "approve":
            con.execute("UPDATE progress SET human_reviewed=1,status='human_reviewed',updated_at=? WHERE learner_id=? AND mission_id=?", (now(),learner_id,mission_id))
    return {"ok":True}

@router.get("/costs/{learner_id}")
def costs(learner_id: str):
    with connect() as con:
        rows = [dict(r) for r in con.execute("SELECT mission_id,purpose,input_tokens,output_tokens,cost_usd,created_at FROM ai_usage WHERE learner_id=? ORDER BY created_at", (learner_id,)).fetchall()]
        total = sum(r["cost_usd"] for r in rows)
    return {"learner_id":learner_id,"total_cost_usd":round(total,6),"usage":rows}

@router.get("/portfolio/{learner_id}", response_class=PlainTextResponse)
def portfolio(learner_id: str): return render_portfolio(learner_id)
