from __future__ import annotations
from datetime import date
from .config import settings
from .db import connect, now

def estimate_tokens(text: str) -> int:
    return max(1, (len(text) + 3) // 4)

def estimate_cost(input_tokens: int, output_tokens: int) -> float:
    return round((input_tokens/1000)*settings.ai_cost_per_1k_input + (output_tokens/1000)*settings.ai_cost_per_1k_output, 8)

def record_usage(learner_id: str, mission_id: int, purpose: str, input_tokens: int, output_tokens: int, cost_usd: float):
    with connect() as con:
        con.execute(
            "INSERT INTO ai_usage(learner_id, mission_id, purpose, input_tokens, output_tokens, cost_usd, created_at) VALUES (?,?,?,?,?,?,?)",
            (learner_id, mission_id, purpose, input_tokens, output_tokens, cost_usd, now()),
        )

def used_tokens_today(learner_id: str) -> int:
    prefix = date.today().isoformat()
    with connect() as con:
        row = con.execute(
            "SELECT COALESCE(SUM(input_tokens+output_tokens),0) AS n FROM ai_usage WHERE learner_id=? AND substr(created_at,1,10)=?",
            (learner_id, prefix),
        ).fetchone()
        return int(row["n"])

def enforce_budget(learner_id: str, planned_tokens: int):
    used = used_tokens_today(learner_id)
    if used + planned_tokens > settings.ai_daily_token_budget:
        raise ValueError(f"Daily AI token budget exceeded ({used}/{settings.ai_daily_token_budget} already used)")
