from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from .missions import list_missions
from .auth import current_learner

router = APIRouter()

STYLE = """
:root{font-family:Inter,ui-sans-serif,system-ui,-apple-system,sans-serif;color:#111827;background:#f6f7f9}body{margin:0}.wrap{max-width:1180px;margin:auto;padding:28px}.top{display:flex;justify-content:space-between;gap:20px;align-items:end}.kicker{font-size:12px;letter-spacing:.12em;text-transform:uppercase;color:#4b5563}.title{font-size:36px;margin:6px 0}.sub{color:#4b5563;max-width:760px}.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(270px,1fr));gap:16px;margin-top:24px}.card{background:white;border:1px solid #e5e7eb;border-radius:16px;padding:18px;box-shadow:0 1px 2px rgba(0,0,0,.04)}.badge{font-size:12px;background:#eef2ff;padding:5px 9px;border-radius:99px;display:inline-block}.skill{font-weight:700;margin:12px 0 6px}.muted{color:#6b7280;font-size:14px}.btn{display:inline-block;margin:8px 6px 0 0;padding:9px 12px;border-radius:9px;background:#111827;color:white;text-decoration:none}.secondary{background:#e5e7eb;color:#111827}.nav a{margin-left:14px;color:#111827}.panel{background:white;border:1px solid #e5e7eb;border-radius:16px;padding:22px;margin-top:20px}textarea,input{width:100%;box-sizing:border-box;padding:10px;border:1px solid #d1d5db;border-radius:8px;margin:6px 0 12px}button{padding:10px 14px;border:0;border-radius:8px;background:#111827;color:white;cursor:pointer}pre{white-space:pre-wrap;background:#111827;color:#f9fafb;padding:14px;border-radius:10px}.warning{border-left:4px solid #f59e0b;padding:10px 12px;background:#fffbeb}.ok{border-left:4px solid #10b981;padding:10px 12px;background:#ecfdf5}label{font-weight:650;display:block;margin-top:10px}table{width:100%;border-collapse:collapse}th,td{text-align:left;padding:9px;border-bottom:1px solid #e5e7eb;font-size:14px}
"""

def page(title, body):
    return f"<!doctype html><html><head><meta charset='utf-8'><meta name='viewport' content='width=device-width,initial-scale=1'><title>{title}</title><style>{STYLE}</style></head><body><div class='wrap'><div class='top'><div><div class='kicker'>Operation: Cyber Ready</div><div class='title'>{title}</div></div><div class='nav'><a href='/'>Learner</a><a href='/progress'>Progress</a><a href='/reviewer'>Reviewer</a><a href='/doctrine'>AI Doctrine</a></div></div>{body}</div></body></html>"

@router.get("/", response_class=HTMLResponse)
def home(request: Request):
    learner=current_learner(request)
    cards=[]
    for m in list_missions():
        cards.append(f"<div class='card'><span class='badge'>Week {m['id']}</span><div class='skill'>{m['title']}</div><div class='muted'>{m['skill']}</div><p>{m['objective']}</p><div class='muted'><b>AI-native:</b> {m['ai_native_dimension']}</div><a class='btn' href='/mission/{m['id']}'>Open</a><a class='btn secondary' href='/api/missions/{m['id']}/starter.zip'>Starter ZIP</a></div>")
    body=f"<p class='sub'>Signed in as <b>{learner}</b>. Real security work with AI present. AI accelerates the work; objective evidence decides whether the work is correct.</p><p><a href='/auth/github'>Use GitHub login</a> · <a href='/auth/logout'>Sign out</a></p><div class='grid'>"+"".join(cards)+"</div>"
    return page("The Range",body)

@router.get("/mission/{mission_id}", response_class=HTMLResponse)
def mission_page(mission_id:int):
    m=list_missions()[mission_id-1]
    qs="".join(f"<li>{q}</li>" for q in m['aar_questions'])
    body=f"""<div class='panel'><span class='badge'>Mission {m['id']}</span><h2>{m['title']}</h2><p>{m['scenario']}</p><div class='warning'><b>AI context:</b> {m['ai_native_dimension']}</div><h3>Objective</h3><p>{m['objective']}</p><h3>Deliverables</h3><ul>{''.join('<li>'+x+'</li>' for x in m['deliverables'])}</ul><h3>Local workflow</h3><pre>range bootstrap {m['id']} --dest ./work/mission-{m['id']:02d}\nrange verify {m['id']} ./work/mission-{m['id']:02d}</pre><a class='btn secondary' href='/api/missions/{m['id']}/starter.zip'>Download starter ZIP</a><a class='btn' href='/aar/{m['id']}'>Complete AAR</a><h3>AAR prompts</h3><ol>{qs}</ol></div>
<div class='panel'><h3>Ask the bounded AI assistant</h3><textarea id='q' rows='5' placeholder='Ask for an explanation, hypothesis, or safe local analysis...'></textarea><button onclick='ask()'>Ask</button><pre id='answer'>No answer yet.</pre></div>
<script>async function ask(){{let q=document.getElementById('q').value;let me=await (await fetch('/api/me')).json();let r=await fetch('/api/assist',{{method:'POST',headers:{{'content-type':'application/json'}},body:JSON.stringify({{learner_id:me.learner_id,mission_id:{m['id']},question:q}})}});document.getElementById('answer').textContent=JSON.stringify(await r.json(),null,2);}}</script>"""
    return page(f"Mission {m['id']}: {m['title']}",body)

@router.get("/aar/{mission_id}", response_class=HTMLResponse)
def aar_page(mission_id:int):
    m=list_missions()[mission_id-1]
    ids=['what','risk','fix','verify','ai','communicate']
    prompts=[
        f"What was the security problem in {m['title']} and what evidence proved it?",
        "What could happen if the issue remained unresolved?",
        "What did you change, and why was that correction proportionate?",
        "How did you verify the result independently of AI output?",
        "Where did AI help, where was it incomplete or wrong, and what remained your responsibility?",
        "Explain the result to a nontechnical manager.",
    ]
    fields=''.join(f"<label>{p}</label><textarea id='{i}' rows='4'></textarea>" for i,p in zip(ids,prompts))
    body=f"""<div class='panel'><p class='warning'>Complete this after deterministic verification. The AAR assesses reasoning; it does not replace technical verification.</p>{fields}<h3>AI Work Record summary</h3><label>What did you ask AI to help with?</label><textarea id='prompts' rows='3'></textarea><label>What AI output did you reject/correct?</label><textarea id='rejected' rows='3'></textarea><label>What objective evidence verified your conclusion?</label><textarea id='evidence' rows='3'></textarea><label>Your final human decision</label><textarea id='decision' rows='3'></textarea><button onclick='submitAAR()'>Submit AAR</button><pre id='result'>Not submitted.</pre></div>
<script>async function submitAAR(){{let me=await (await fetch('/api/me')).json();let answers={{}};for(let id of {ids!r}) answers[id]=document.getElementById(id).value;let body={{learner_id:me.learner_id,mission_id:{mission_id},answers:answers,ai_work_record:{{mission_id:{mission_id},prompts_or_tasks:[document.getElementById('prompts').value],accepted_outputs:[],rejected_outputs:[document.getElementById('rejected').value],verification_evidence:[document.getElementById('evidence').value],human_decision:document.getElementById('decision').value}}}};let r=await fetch('/api/aar/submit',{{method:'POST',headers:{{'content-type':'application/json'}},body:JSON.stringify(body)}});document.getElementById('result').textContent=JSON.stringify(await r.json(),null,2);}}</script>"""
    return page(f"Mission {mission_id} AAR",body)

@router.get("/progress", response_class=HTMLResponse)
def progress_page(request: Request):
    learner=current_learner(request)
    body=f"""<div class='panel'><p>Progress for <b>{learner}</b></p><button onclick='load()'>Refresh</button><div id='out'></div></div><script>async function load(){{let r=await fetch('/api/progress/{learner}');let d=await r.json();document.getElementById('out').innerHTML='<table><tr><th>Mission</th><th>Status</th><th>Verified</th><th>AAR</th><th>Human review</th></tr>'+d.map(x=>`<tr><td>${{x.mission_id}}</td><td>${{x.status}}</td><td>${{x.verifier_passed?'Yes':'No'}}</td><td>${{x.aar_score??'—'}}</td><td>${{x.human_reviewed?'Yes':'No'}}</td></tr>`).join('')+'</table>';}}load()</script>"""
    return page("Learner Progress",body)

@router.get("/doctrine", response_class=HTMLResponse)
def doctrine():
    body="""<div class='panel'><h2>AI may assist; AI may not be the authority.</h2><h3>Use AI to</h3><p>Accelerate research, explain unfamiliar code/configuration, generate hypotheses, draft scripts/queries, compare policies, summarize logs, draft findings, and challenge assumptions.</p><h3>Never treat AI as authority to</h3><p>Declare a system secure, approve production, establish that a control works, determine authorization, establish evidence, or make an unverified material risk decision.</p><h3>Always</h3><p>Verify material claims, test results, inspect source/configuration/evidence, preserve evidence, understand model/tool context, and document when AI output was rejected or corrected.</p></div>"""
    return page("AI Operating Doctrine",body)

@router.get("/reviewer", response_class=HTMLResponse)
def reviewer():
    body="""<div class='panel'><p>The reviewer console intentionally reads only minimum indexed progress. Learner repositories remain the primary evidence record.</p><button onclick='load()'>Load learner status</button><pre id='data'>Not loaded.</pre></div><script>async function load(){let r=await fetch('/api/review/learners');document.getElementById('data').textContent=JSON.stringify(await r.json(),null,2)}</script>"""
    return page("Reviewer Console",body)
