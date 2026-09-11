# Cost Model

The V1 application records estimated input/output tokens and cost for learner assistance and AAR interactions.

Default example rates are intentionally low placeholders and must be replaced with the selected provider's real rates before a pilot.

Target: **less than $50 total model/infrastructure cost for an 8-person, 16-week cohort**, excluding human labor.

Controls:
- per-learner daily token budget
- local no-cost fallback provider
- no persistent cloud lab requirement
- GitHub/devcontainer/local Docker execution
- SQLite index
- concise AAR prompts

Run `GET /api/costs/{learner_id}` to inspect usage.
