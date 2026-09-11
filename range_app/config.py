from dataclasses import dataclass
from pathlib import Path
import os

@dataclass(frozen=True)
class Settings:
    env: str = os.getenv("RANGE_ENV", "development")
    db_path: Path = Path(os.getenv("RANGE_DB_PATH", "./range.db"))
    ai_provider: str = os.getenv("RANGE_AI_PROVIDER", "local")
    ai_daily_token_budget: int = int(os.getenv("RANGE_AI_DAILY_TOKEN_BUDGET", "12000"))
    ai_cost_per_1k_input: float = float(os.getenv("RANGE_AI_COST_PER_1K_INPUT", "0.00015"))
    ai_cost_per_1k_output: float = float(os.getenv("RANGE_AI_COST_PER_1K_OUTPUT", "0.00060"))
    ai_base_url: str = os.getenv("RANGE_AI_BASE_URL", "")
    ai_api_key: str = os.getenv("RANGE_AI_API_KEY", "")
    ai_model: str = os.getenv("RANGE_AI_MODEL", "")
    session_secret: str = os.getenv("RANGE_SESSION_SECRET", "dev-only-change-me")

settings = Settings()
