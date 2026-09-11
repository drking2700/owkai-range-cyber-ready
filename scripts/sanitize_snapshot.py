#!/usr/bin/env python3
from pathlib import Path
import shutil, sys, re
if len(sys.argv)!=3:
    print('usage: sanitize_snapshot.py <src> <dest>'); raise SystemExit(2)
src,dst=map(Path,sys.argv[1:])
if dst.exists(): shutil.rmtree(dst)
shutil.copytree(src,dst,ignore=shutil.ignore_patterns('.git','.env','*.pem','*.key','*.p12','*.pfx'))
# Remove obvious URLs/hostnames that look production-specific from text snapshots.
for p in dst.rglob('*'):
    if not p.is_file() or p.stat().st_size>1_000_000: continue
    try: t=p.read_text(encoding='utf-8')
    except Exception: continue
    t=re.sub(r'https://[A-Za-z0-9.-]+\.(?:com|net|org)(?:/[^\s]*)?', 'https://training.invalid/', t)
    p.write_text(t,encoding='utf-8')
print(dst)
