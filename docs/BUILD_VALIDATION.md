# Build Validation — September 10, 2026

## Automated test suite

`PYTHONPATH=. pytest -q`

**Result: 12 passed.**

Coverage includes:
- all 16 mission manifests present and AI-native
- human-review checkpoints at missions 8/12/16
- Mission 1 fail → corrected pass
- Mission 5 fail → corrected pass
- Mission 9 fail → corrected pass
- Mission 11 evidence-hash validation
- all 16 missions have a known passing state
- prompt-injection guard
- seeded flawed AI response remains explicitly non-authoritative
- API health and 16-mission inventory
- starter ZIP delivery
- repository real-secret pattern check

## Secret scan

`python scripts/secret_scan.py .`

**Result: passed.**

Synthetic `TRAINING-*` values are intentional fixtures and are not treated as real credentials.

## Portal smoke test

Local FastAPI server started successfully.

Verified:
- `/api/health` returned `ok`
- `/api/missions` returned 16 missions
- learner home page rendered successfully

## Synthetic vertical-slice dry run

`scripts/vertical_slice_dry_run.py`

Three synthetic learners each completed the technical flow for:

**Mission 1 → Mission 5 → Mission 9**

For all nine runs:
- starter state failed verification as expected
- corrected state passed verification
- AI Work Record was required

**Result: passed.**

This is a technical dry run only. It does **not** satisfy the Gate 2 requirement for actual technical/nontechnical human learners, AAR usability evidence, independent Claude review, or measured external-provider cost.

## Repository import validation — September 11, 2026

Source: `Operation_Cyber_Ready_Range_V1.zip`.

- SHA-256: `43fd8e08008a1c5fc663f255722aacc0ad42da1d2ca45bfce35eb0078b18cc73`.
- Archive matches the ZIP previously uploaded in commit `0233baa`.
- All 109 source files were extracted at the repository root and compared byte-for-byte before fixes.
- All 16 mission directories include their manifest, brief, and starter assets; dotfiles and training log fixtures are present.
- `.github/workflows/ci.yml` is at the repository root, where GitHub Actions can discover it.

A fresh Python 3.12 virtual environment reproduced a test-collection failure:
`ModuleNotFoundError: No module named 'itsdangerous'`. The application imports
Starlette's session middleware, which requires this optional package. Added
`itsdangerous==2.2.0` as a runtime dependency and repeated installation and checks.
Generated Python package/build output is now excluded from Git.

Local results after the fix:

- `python -m pip install -e '.[dev]'`: passed.
- `python -m pytest`: **12 passed**, with one upstream Starlette/AnyIO deprecation warning.
- `python scripts/secret_scan.py .`: passed.
- `python scripts/vertical_slice_dry_run.py`: all nine Mission 1/5/9 runs reported starter failure and corrected success.

These results validate the import and existing automated checks; formal independent review and Gate 2 remain pending. GitHub Actions results are recorded on the pull request.
