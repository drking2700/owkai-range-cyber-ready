# Gate 1 Evidence Package

## Product baseline
- PRD v0.2 AI-native direction: approved by build instruction on 2026-09-10 for implementation work.
- AI Operating Doctrine: implemented in product and curriculum.
- AI-native mapping: present in every mission manifest.
- Missions 1/5/9: implementation-ready and runnable.

## Training asset safety
- Local synthetic training values only.
- No production endpoints or credentials.
- Secret scanner distinguishes approved `TRAINING-*` fixtures from accidental real-secret patterns.
- GitHub Actions runs tests + scanner.

## Verification standard
- Every mission includes deterministic verification rules.
- `ai_work_record.json` is required.
- No model response can set verifier state.
- Mission 1 and Mission 9 deliberately contain flawed AI advice.

## AI access model
- Local fallback provider works with no external model.
- External OpenAI-compatible provider is opt-in only.
- No model tool execution.
- Per-learner daily token budget enforced.
- Usage/cost ledger stored separately from mission evidence.

## Privacy
- Minimum indexed learner data.
- Veteran self-identification is optional.
- Repositories/workspaces remain the primary evidence record.
- Provider-retention review remains a deployment decision before external pilot if an external provider is enabled.

## Remaining human/external approvals
- Independent Claude review is not represented by this build artifact and must be performed separately.
- Philadelphia pilot confirmation and grant/VA pathways remain external program decisions.
