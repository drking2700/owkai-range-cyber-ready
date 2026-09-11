from __future__ import annotations
import sqlite3
from pathlib import Path
from datetime import datetime, timezone
from .config import settings

SCHEMA = """
PRAGMA foreign_keys=ON;
CREATE TABLE IF NOT EXISTS learners (
  id TEXT PRIMARY KEY,
  display_name TEXT NOT NULL,
  email TEXT,
  veteran_self_id INTEGER,
  consent_at TEXT,
  created_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS progress (
  learner_id TEXT NOT NULL,
  mission_id INTEGER NOT NULL,
  status TEXT NOT NULL,
  verifier_passed INTEGER NOT NULL DEFAULT 0,
  aar_score REAL,
  human_reviewed INTEGER NOT NULL DEFAULT 0,
  updated_at TEXT NOT NULL,
  PRIMARY KEY (learner_id, mission_id),
  FOREIGN KEY (learner_id) REFERENCES learners(id) ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS aar_records (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  learner_id TEXT NOT NULL,
  mission_id INTEGER NOT NULL,
  transcript_json TEXT NOT NULL,
  scores_json TEXT NOT NULL,
  created_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS ai_usage (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  learner_id TEXT NOT NULL,
  mission_id INTEGER NOT NULL,
  purpose TEXT NOT NULL,
  input_tokens INTEGER NOT NULL,
  output_tokens INTEGER NOT NULL,
  cost_usd REAL NOT NULL,
  created_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS human_reviews (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  learner_id TEXT NOT NULL,
  mission_id INTEGER NOT NULL,
  reviewer TEXT NOT NULL,
  decision TEXT NOT NULL,
  notes TEXT,
  created_at TEXT NOT NULL
);
"""

def now():
    return datetime.now(timezone.utc).isoformat()

def connect(path: Path | None = None):
    p = path or settings.db_path
    con = sqlite3.connect(p)
    con.row_factory = sqlite3.Row
    return con

def init_db(path: Path | None = None):
    with connect(path) as con:
        con.executescript(SCHEMA)

def seed_demo(path: Path | None = None):
    init_db(path)
    with connect(path) as con:
        con.execute(
            "INSERT OR IGNORE INTO learners(id, display_name, email, veteran_self_id, consent_at, created_at) VALUES (?,?,?,?,?,?)",
            ("demo", "Demo Learner", "demo@example.invalid", None, now(), now()),
        )
        for mid in range(1,17):
            con.execute(
                "INSERT OR IGNORE INTO progress(learner_id, mission_id, status, verifier_passed, updated_at) VALUES (?,?,?,?,?)",
                ("demo", mid, "not_started", 0, now()),
            )

def ensure_learner(learner_id: str, display_name: str | None = None):
    with connect() as con:
        row = con.execute("SELECT id FROM learners WHERE id=?", (learner_id,)).fetchone()
        if not row:
            con.execute(
                "INSERT INTO learners(id, display_name, created_at) VALUES (?,?,?)",
                (learner_id, display_name or learner_id, now()),
            )
            for mid in range(1,17):
                con.execute(
                    "INSERT OR IGNORE INTO progress(learner_id, mission_id, status, updated_at) VALUES (?,?,?,?)",
                    (learner_id, mid, "not_started", now()),
                )
