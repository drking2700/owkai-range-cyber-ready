from __future__ import annotations
from pathlib import Path
import json, hashlib, re
from .missions import load_manifest
from .models import AIWorkRecord

class VerificationError(Exception):
    pass

def _read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))

def _dot(obj, path: str):
    cur = obj
    for part in path.split("."):
        if isinstance(cur, list):
            cur = cur[int(part)]
        else:
            cur = cur[part]
    return cur

def validate_ai_work_record(workspace: Path, mission_id: int) -> list[str]:
    errors = []
    p = workspace / "ai_work_record.json"
    if not p.exists():
        return ["ai_work_record.json is required"]
    try:
        rec = AIWorkRecord.model_validate_json(p.read_text(encoding="utf-8"))
        if rec.mission_id != mission_id:
            errors.append(f"AI Work Record mission_id must be {mission_id}")
    except Exception as e:
        errors.append(f"AI Work Record invalid: {e}")
    return errors

def verify(mission_id: int, workspace: Path) -> dict:
    manifest = load_manifest(mission_id)
    errors = validate_ai_work_record(workspace, mission_id)
    evidence = []
    for rule in manifest.get("verification", []):
        t = rule["type"]
        rel = rule.get("file")
        p = workspace / rel if rel else None
        try:
            if t == "file_exists":
                if not p.exists(): errors.append(rule["message"])
                else: evidence.append(f"exists:{rel}")
            elif t == "file_not_contains":
                if not p.exists() or rule["value"] in p.read_text(encoding="utf-8"):
                    errors.append(rule["message"])
                else: evidence.append(f"not_contains:{rel}:{rule['value']}")
            elif t == "file_contains":
                if not p.exists() or rule["value"] not in p.read_text(encoding="utf-8"):
                    errors.append(rule["message"])
                else: evidence.append(f"contains:{rel}:{rule['value']}")
            elif t == "json_equals":
                if not p.exists() or _dot(_read_json(p), rule["path"]) != rule["value"]:
                    errors.append(rule["message"])
                else: evidence.append(f"json_equals:{rel}:{rule['path']}")
            elif t == "json_in":
                if not p.exists() or _dot(_read_json(p), rule["path"]) not in rule["values"]:
                    errors.append(rule["message"])
                else: evidence.append(f"json_in:{rel}:{rule['path']}")
            elif t == "json_lte":
                if not p.exists() or float(_dot(_read_json(p), rule["path"])) > float(rule["value"]):
                    errors.append(rule["message"])
                else: evidence.append(f"json_lte:{rel}:{rule['path']}")
            elif t == "json_gte":
                if not p.exists() or float(_dot(_read_json(p), rule["path"])) < float(rule["value"]):
                    errors.append(rule["message"])
                else: evidence.append(f"json_gte:{rel}:{rule['path']}")
            elif t == "json_list_exact":
                got = _dot(_read_json(p), rule["path"]) if p and p.exists() else None
                if got != rule["value"]:
                    errors.append(rule["message"])
                else: evidence.append(f"json_list_exact:{rel}:{rule['path']}")
            elif t == "json_no_wildcard":
                got = _dot(_read_json(p), rule["path"]) if p and p.exists() else None
                vals = got if isinstance(got, list) else [got]
                if any(v == "*" or (isinstance(v,str) and "*" in v) for v in vals):
                    errors.append(rule["message"])
                else: evidence.append(f"json_no_wildcard:{rel}:{rule['path']}")
            elif t == "min_text_length":
                txt = p.read_text(encoding="utf-8") if p and p.exists() else ""
                if len(txt.strip()) < int(rule["value"]): errors.append(rule["message"])
                else: evidence.append(f"min_text_length:{rel}")
            elif t == "regex":
                txt = p.read_text(encoding="utf-8") if p and p.exists() else ""
                if not re.search(rule["pattern"], txt, re.I|re.M): errors.append(rule["message"])
                else: evidence.append(f"regex:{rel}")
            elif t == "sha256_manifest":
                mp = p
                if not mp.exists():
                    errors.append(rule["message"]); continue
                data = _read_json(mp)
                for entry in data.get("files", []):
                    fp = workspace / entry["path"]
                    if not fp.exists():
                        errors.append(f"Evidence file missing: {entry['path']}"); continue
                    actual = hashlib.sha256(fp.read_bytes()).hexdigest()
                    if actual != entry.get("sha256"):
                        errors.append(f"Hash mismatch: {entry['path']}")
                if not errors: evidence.append("sha256_manifest:validated")
            else:
                errors.append(f"Unknown verifier rule: {t}")
        except Exception as e:
            errors.append(f"Verifier error for {rel or t}: {e}")
    return {
        "mission_id": mission_id,
        "passed": not errors,
        "errors": errors,
        "evidence": evidence,
        "principle": "AI output never counts as sole verification evidence.",
    }
