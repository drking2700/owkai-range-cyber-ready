from pathlib import Path
import json, hashlib
from range_app.missions import bootstrap
from range_app.verification import verify


def complete_record(path: Path, mission_id: int):
    p=path/'ai_work_record.json'
    d=json.loads(p.read_text())
    d.update({
      'mission_id':mission_id,
      'prompts_or_tasks':['Asked AI to explain the local training configuration.'],
      'accepted_outputs':['Used a hypothesis only.'],
      'rejected_outputs':['Rejected any claim not supported by local evidence.'],
      'verification_evidence':['Ran deterministic verifier and inspected changed local file.'],
      'human_decision':'I made the final security decision after checking objective local evidence.'
    })
    p.write_text(json.dumps(d,indent=2))


def test_mission1_fails_then_passes(tmp_path):
    ws=tmp_path/'m1'; bootstrap(1,ws); complete_record(ws,1)
    assert verify(1,ws)['passed'] is False
    cfg=json.loads((ws/'config.json').read_text()); cfg['api_key']='${APP_API_KEY}'; (ws/'config.json').write_text(json.dumps(cfg))
    (ws/'.env.example').write_text('APP_API_KEY=\n')
    assert verify(1,ws)['passed'] is True


def test_mission5_fails_then_passes(tmp_path):
    ws=tmp_path/'m5'; bootstrap(5,ws); complete_record(ws,5)
    assert not verify(5,ws)['passed']
    d=json.loads((ws/'api_policy.json').read_text()); d['rate_limit']={'enabled':True,'scope':'identity','per_minute':60,'burst':10}; (ws/'api_policy.json').write_text(json.dumps(d))
    assert verify(5,ws)['passed']


def test_mission9_fails_then_passes(tmp_path):
    ws=tmp_path/'m9'; bootstrap(9,ws); complete_record(ws,9)
    assert not verify(9,ws)['passed']
    d=json.loads((ws/'policy.json').read_text()); d['Statement'][0]['Action']=['s3:GetObject']; d['Statement'][0]['Resource']=['arn:aws:s3:::training-evidence/mission9/*']; (ws/'policy.json').write_text(json.dumps(d))
    assert verify(9,ws)['passed']


def test_mission11_hash_manifest(tmp_path):
    ws=tmp_path/'m11'; bootstrap(11,ws); complete_record(ws,11)
    files=[]
    for rel in ['event.log','config_snapshot.json']:
        files.append({'path':rel,'sha256':hashlib.sha256((ws/rel).read_bytes()).hexdigest()})
    (ws/'evidence_manifest.json').write_text(json.dumps({'collected_at':'2026-09-10T00:00:00Z','tool_version':'test','files':files}))
    assert verify(11,ws)['passed']
