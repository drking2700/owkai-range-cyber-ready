#!/usr/bin/env python3
from pathlib import Path
import re, sys

ROOT = Path(sys.argv[1] if len(sys.argv)>1 else ".").resolve()
SKIP = {'.git','.venv','__pycache__','.pytest_cache'}
# Synthetic TRAINING-* values are approved mission fixtures and are excluded.
PATTERNS = {
  'aws_access_key': re.compile(r'\bAKIA[0-9A-Z]{16}\b'),
  'private_key': re.compile(r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----'),
  'github_token': re.compile(r'\bgh[pousr]_[A-Za-z0-9]{30,}\b'),
  'generic_bearer': re.compile(r'(?i)authorization\s*[:=]\s*bearer\s+[A-Za-z0-9._-]{20,}'),
}
findings=[]
for p in ROOT.rglob('*'):
    if not p.is_file() or any(part in SKIP for part in p.parts): continue
    if p.stat().st_size > 2_000_000: continue
    try: text=p.read_text(encoding='utf-8')
    except Exception: continue
    for name,pat in PATTERNS.items():
        for m in pat.finditer(text):
            findings.append((str(p.relative_to(ROOT)),name,m.group(0)[:20]+'...'))
if findings:
    print('Potential secrets found:')
    for f in findings: print(*f, sep=' | ')
    raise SystemExit(1)
print('secret scan passed')
