from pathlib import Path
import json, hashlib
from range_app.missions import bootstrap
from range_app.verification import verify


def record(ws, mid):
    p=ws/'ai_work_record.json'; d=json.loads(p.read_text())
    d.update({'mission_id':mid,'prompts_or_tasks':['Asked AI for a hypothesis.'],'accepted_outputs':['Used only as a hypothesis.'],'rejected_outputs':['Rejected unsupported claims.'],'verification_evidence':['Inspected local file and ran deterministic verifier.'],'human_decision':'I made the final decision after independently checking the local objective evidence.'})
    p.write_text(json.dumps(d,indent=2))

def solve(mid, ws):
    record(ws,mid)
    if mid==1:
        d=json.loads((ws/'config.json').read_text());d['api_key']='${APP_API_KEY}';(ws/'config.json').write_text(json.dumps(d));(ws/'.env.example').write_text('APP_API_KEY=\n')
    elif mid==2:(ws/'sudoers.conf').write_text('analyst ALL=(root) /usr/bin/journalctl\n')
    elif mid==3:
        d=json.loads((ws/'service.json').read_text());d['admin']['host']='127.0.0.1';(ws/'service.json').write_text(json.dumps(d))
    elif mid==4:
        (ws/'revoked_secrets.json').write_text(json.dumps({'TRAINING-GIT-SECRET-7788':'revoked'}));(ws/'remediation.md').write_text('# Remediation\nRotate and revoke the exposed credential, then rewrite repository history and verify no copies remain.\n')
    elif mid==5:(ws/'api_policy.json').write_text(json.dumps({'rate_limit':{'enabled':True,'scope':'identity','per_minute':60,'burst':10}}))
    elif mid==6:(ws/'telemetry.json').write_text(json.dumps({'request_fields':['actor_id','user_agent','path','outcome'],'enumeration':{'alert_after_requests':25}}))
    elif mid==7:(ws/'audit_policy.json').write_text(json.dumps({'tool_actions':{'audit_required':True,'sink':'append_only'}}))
    elif mid==8:(ws/'logging.json').write_text(json.dumps({'format':'json','sink':'append_only','fields':['actor','action','outcome']}))
    elif mid==9:(ws/'policy.json').write_text(json.dumps({'Version':'2012-10-17','Statement':[{'Effect':'Allow','Action':['s3:GetObject'],'Resource':['arn:aws:s3:::training-evidence/mission9/*']}]}))
    elif mid==10:(ws/'authz.json').write_text(json.dumps({'tenant_source':'token_claim','enforce_subject_resource_match':True}))
    elif mid==11:
        files=[{'path':r,'sha256':hashlib.sha256((ws/r).read_bytes()).hexdigest()} for r in ['event.log','config_snapshot.json']]
        (ws/'evidence_manifest.json').write_text(json.dumps({'collected_at':'2026-09-10T00:00:00Z','tool_version':'test','files':files}))
    elif mid==12:(ws/'tool_policy.json').write_text(json.dumps({'allowed_tools':['kb.search','ticket.read'],'default':'deny','require_confirmation_for_write':True}))
    elif mid==13:(ws/'assessment.md').write_text('# Evidence\nEVID-101 shows wildcard IAM. EVID-102 shows stdout-only logs.\n# Risk\nExcess authority increases blast radius.\n# Recommendation\nApply least privilege and durable logging.\n# Verification\nRe-run policy and logging checks against EVID-101 and EVID-102.\n')
    elif mid==14:(ws/'analysis_review.json').write_text(json.dumps({'claims':[{'claim':1,'decision':'reject','evidence':'EVID-201'},{'claim':2,'decision':'accept','evidence':'EVID-202'},{'claim':3,'decision':'reject','evidence':'EVID-203'},{'claim':4,'decision':'accept','evidence':'EVID-204'}]}))
    elif mid==15:(ws/'recommendations.md').write_text('# Remediation Plan\nPriority: High\nOwner: Platform Security\nValidation: deterministic IAM and logging tests.\nResidual Risk: integrations may add new permissions and require reassessment.\n\nImplement least privilege for agent identity first because excessive authority creates direct blast-radius risk. Add durable append-only audit records second so actions can be investigated. Apply per-identity rate limits after confirming expected business throughput. Each item requires named ownership, a due date in the delivery system, and repeatable validation evidence before closure. This plan replaces generic AI advice with specific accountable decisions and measurable verification.\n')
    elif mid==16:(ws/'interview_answers.md').write_text('# Mock Interview\n\n## Finding\nI identified excessive agent permissions using the local IAM policy as evidence. The issue was not the model opinion; the wildcard actions and resources were directly observable.\n\n## Risk\nThe risk was unnecessary blast radius: a compromised or misdirected agent could access unrelated resources.\n\n## Verification\nI replaced the wildcard policy with one read action on one training path and ran deterministic verification.\n\n## AI Use\nAI helped generate hypotheses, but I rejected its claim that wildcard access was acceptable in a training environment and verified the policy myself.\n\n## Uncertainty\nIn a real system I would still validate runtime identity assumptions, inherited permissions, service control policies, session boundaries, and audit coverage before claiming the effective permission set was fully understood.\n')


def test_every_mission_has_a_known_passing_state(tmp_path):
    failures=[]
    for mid in range(1,17):
        ws=tmp_path/f'm{mid:02d}';bootstrap(mid,ws);solve(mid,ws);r=verify(mid,ws)
        if not r['passed']: failures.append((mid,r['errors']))
    assert failures==[]
