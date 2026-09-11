from .db import connect
from .missions import list_missions

def render_portfolio(learner_id: str) -> str:
    with connect() as con:
        rows = {r["mission_id"]: r for r in con.execute("SELECT * FROM progress WHERE learner_id=?", (learner_id,)).fetchall()}
    lines = [f"# Operation: Cyber Ready Portfolio — {learner_id}", "", "AI-native, human-accountable security work.", ""]
    for m in list_missions():
        r = rows.get(m["id"])
        status = r["status"] if r else "not_started"
        score = r["aar_score"] if r and r["aar_score"] is not None else "—"
        lines += [f"## Mission {m['id']}: {m['title']}", f"- Skill: {m['skill']}", f"- Status: {status}", f"- AAR score: {score}", f"- AI-native dimension: {m['ai_native_dimension']}", ""]
    return "\n".join(lines)
