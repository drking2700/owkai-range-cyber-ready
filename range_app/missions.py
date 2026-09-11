from __future__ import annotations
from pathlib import Path
import json, shutil

REPO_ROOT = Path(__file__).resolve().parents[1]
MISSIONS_ROOT = REPO_ROOT / "missions"

def mission_dir(mission_id: int) -> Path:
    return MISSIONS_ROOT / f"{mission_id:02d}"

def load_manifest(mission_id: int) -> dict:
    path = mission_dir(mission_id) / "manifest.json"
    if not path.exists():
        raise KeyError(f"Mission {mission_id} not found")
    return json.loads(path.read_text(encoding="utf-8"))

def list_missions() -> list[dict]:
    return [load_manifest(i) for i in range(1,17)]

def bootstrap(mission_id: int, dest: Path) -> Path:
    src = mission_dir(mission_id) / "starter"
    if dest.exists() and any(dest.iterdir()):
        raise FileExistsError(f"Destination not empty: {dest}")
    dest.mkdir(parents=True, exist_ok=True)
    for item in src.iterdir():
        if item.is_dir():
            shutil.copytree(item, dest / item.name)
        else:
            shutil.copy2(item, dest / item.name)
    template = REPO_ROOT / "schemas" / "ai_work_record.template.json"
    shutil.copy2(template, dest / "ai_work_record.json")
    return dest
