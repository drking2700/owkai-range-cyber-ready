from pathlib import Path
import re

def test_no_real_secret_patterns_in_repository():
    root=Path(__file__).resolve().parents[1]
    patterns=[re.compile(r'\bAKIA[0-9A-Z]{16}\b'),re.compile(r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----')]
    findings=[]
    for p in root.rglob('*'):
        if not p.is_file() or any(x in p.parts for x in ['.git','.venv','__pycache__']): continue
        try:t=p.read_text(encoding='utf-8')
        except:continue
        for pat in patterns:
            if pat.search(t): findings.append(str(p))
    assert not findings
