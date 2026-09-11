#!/usr/bin/env python3
from pathlib import Path
import tempfile, json
from range_app.missions import bootstrap
from range_app.verification import verify


def record(ws, mid):
    p=ws/'ai_work_record.json'; d=json.loads(p.read_text())
    d.update({
        'mission_id':mid,
        'prompts_or_tasks':['Used AI to form a hypothesis about the local training issue.'],
        'accepted_outputs':['Accepted only statements confirmed by local evidence.'],
        'rejected_outputs':['Rejected unsafe or unsupported model conclusions.'],
        'verification_evidence':['Inspected local configuration and ran deterministic verification.'],
        'human_decision':'I retained responsibility for the final decision and verified the material claim independently.'
    });p.write_text(json.dumps(d,indent=2))

def solve(mid,ws):
    record(ws,mid)
    if mid==1:
        d=json.loads((ws/'config.json').read_text());d['api_key']='${APP_API_KEY}';(ws/'config.json').write_text(json.dumps(d));(ws/'.env.example').write_text('APP_API_KEY=\n')
    elif mid==5:
        (ws/'api_policy.json').write_text(json.dumps({'rate_limit':{'enabled':True,'scope':'identity','per_minute':60,'burst':10}}))
    elif mid==9:
        (ws/'policy.json').write_text(json.dumps({'Version':'2012-10-17','Statement':[{'Effect':'Allow','Action':['s3:GetObject'],'Resource':['arn:aws:s3:::training-evidence/mission9/*']}]}))

report={'kind':'synthetic technical dry run','human_learner':False,'learners':[]}
with tempfile.TemporaryDirectory() as td:
    base=Path(td)
    for learner in ['synthetic-a','synthetic-b','synthetic-c']:
        lr={'learner_id':learner,'missions':[]}
        for mid in [1,5,9]:
            ws=base/learner/f'mission-{mid:02d}';bootstrap(mid,ws)
            before=verify(mid,ws)
            solve(mid,ws)
            after=verify(mid,ws)
            lr['missions'].append({'mission_id':mid,'starter_failed':not before['passed'],'solved_passed':after['passed'],'errors_after':after['errors']})
        report['learners'].append(lr)
report['passed']=all(m['starter_failed'] and m['solved_passed'] for l in report['learners'] for m in l['missions'])
print(json.dumps(report,indent=2))
