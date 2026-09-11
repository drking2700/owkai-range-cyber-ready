# Operation: Cyber Ready — The Range

AI-native, human-accountable cybersecurity training range for veterans and career-transition learners.

## What this repository contains

- 16 mission curriculum with AI-native dimensions
- deterministic mission verification
- learner AI-assistance interface with a local safe fallback provider
- AI Work Record evidence model
- after-action review (AAR) workflow and scoring
- learner portal and reviewer console
- SQLite progress/evidence index
- cost ledger and budget controls
- devcontainer / local Docker development environment
- GitHub Actions CI
- secret scanning and prompt-injection safety tests
- portfolio generation

## Design doctrine

**AI may assist; AI may not be the authority.** A learner can use AI for research, analysis, scripting, investigation, and drafting, but no mission passes because a model says it should. Objective verification and preserved evidence determine completion.

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
pip install -e '.[dev]'
range init-db
range seed-demo
range serve
```

Open http://127.0.0.1:8000

### Try a mission locally

```bash
range bootstrap 1 --dest ./work/mission-01
range verify 1 ./work/mission-01
```

The starter state should fail. Fix the issue, complete `ai_work_record.json`, then run the verifier again.

## Default AI mode

The repository works without an API key. `RANGE_AI_PROVIDER=local` uses a deterministic local coaching/assistant provider suitable for development and pilots where external model access is unavailable.

An OpenAI-compatible provider adapter is included but disabled unless explicitly configured. The application never executes model-proposed tools or shell commands.

## Repository layout

- `range_app/` — API, portal, reviewer console, DB, AI/AAR services
- `missions/` — 16 mission packages
- `schemas/` — learner evidence schemas
- `scripts/` — sanitization, secret scanning, portfolio tools
- `tests/` — product/security tests
- `docs/` — architecture, Gate 1 evidence, pilot operations

## Safety boundary

This range contains intentionally insecure **local training files and configurations only**. It does not include production credentials, live targets, exploit delivery, persistence tooling, or instructions to attack third-party systems.
