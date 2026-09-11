from fastapi.testclient import TestClient
import tempfile
from pathlib import Path
import range_app.db as db
import range_app.api as api
import range_app.aar as aar
from range_app.main import app


def test_health_and_missions(tmp_path, monkeypatch):
    # Redirect DB connect for this test process.
    original=db.connect
    def conn(path=None): return original(tmp_path/'test.db')
    monkeypatch.setattr(db,'connect',conn)
    monkeypatch.setattr(api,'connect',conn)
    monkeypatch.setattr(aar,'connect',conn)
    db.init_db(tmp_path/'test.db'); db.seed_demo(tmp_path/'test.db')
    c=TestClient(app)
    assert c.get('/api/health').status_code==200
    r=c.get('/api/missions'); assert r.status_code==200 and len(r.json())==16

def test_starter_zip_download(tmp_path, monkeypatch):
    original=db.connect
    def conn(path=None): return original(tmp_path/'test2.db')
    monkeypatch.setattr(db,'connect',conn); monkeypatch.setattr(api,'connect',conn); monkeypatch.setattr(aar,'connect',conn)
    db.init_db(tmp_path/'test2.db'); db.seed_demo(tmp_path/'test2.db')
    c=TestClient(app)
    r=c.get('/api/missions/1/starter.zip')
    assert r.status_code==200
    assert r.headers['content-type']=='application/zip'
    assert len(r.content)>100
