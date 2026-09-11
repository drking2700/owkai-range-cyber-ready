from __future__ import annotations
import argparse, json
from pathlib import Path
import uvicorn
from .db import init_db, seed_demo
from .missions import bootstrap, list_missions
from .verification import verify
from .portfolio import render_portfolio


def main():
    p=argparse.ArgumentParser(prog="range")
    sub=p.add_subparsers(dest="cmd",required=True)
    sub.add_parser("init-db")
    sub.add_parser("seed-demo")
    s=sub.add_parser("serve"); s.add_argument("--host",default="127.0.0.1"); s.add_argument("--port",type=int,default=8000)
    b=sub.add_parser("bootstrap"); b.add_argument("mission_id",type=int); b.add_argument("--dest",required=True)
    v=sub.add_parser("verify"); v.add_argument("mission_id",type=int); v.add_argument("workspace")
    sub.add_parser("missions")
    pf=sub.add_parser("portfolio"); pf.add_argument("learner_id")
    a=p.parse_args()
    if a.cmd=="init-db": init_db(); print("database initialized")
    elif a.cmd=="seed-demo": seed_demo(); print("demo learner seeded")
    elif a.cmd=="serve": uvicorn.run("range_app.main:app",host=a.host,port=a.port,reload=False)
    elif a.cmd=="bootstrap": print(bootstrap(a.mission_id,Path(a.dest)))
    elif a.cmd=="verify":
        result=verify(a.mission_id,Path(a.workspace)); print(json.dumps(result,indent=2)); raise SystemExit(0 if result["passed"] else 1)
    elif a.cmd=="missions":
        for m in list_missions(): print(f"{m['id']:02d} {m['title']} — {m['skill']}")
    elif a.cmd=="portfolio": print(render_portfolio(a.learner_id))

if __name__=="__main__": main()
