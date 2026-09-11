import os
from pathlib import Path
import pytest

@pytest.fixture(autouse=True)
def isolated_db(tmp_path, monkeypatch):
    # Change already-imported settings object field is frozen, so tests that need DB use module-specific monkeypatch below.
    yield
