#!/usr/bin/env python3
from pathlib import Path
import hashlib, json, sys
from datetime import datetime, timezone
if len(sys.argv)<3:
    print('usage: generate_evidence_manifest.py <workspace> <file> [file...]'); raise SystemExit(2)
root=Path(sys.argv[1])
files=[]
for rel in sys.argv[2:]:
    p=root/rel
    files.append({'path':rel,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
out={'collected_at':datetime.now(timezone.utc).isoformat(),'tool_version':'range-evidence/0.1','files':files}
(root/'evidence_manifest.json').write_text(json.dumps(out,indent=2)+'\n')
print(root/'evidence_manifest.json')
