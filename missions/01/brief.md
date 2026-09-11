# Mission 1: Plaintext

**Phase:** A  
**Core skill:** Secrets / data exposure  

## Situation
A small internal service was assembled quickly. An AI assistant claims the exposed string is only a harmless example value.

## Objective
Remove the plaintext credential from the committed configuration and replace it with an environment-variable reference while documenting independent verification.

## AI context
AI proposes that the visible credential is a non-sensitive sample. The learner must prove whether it is a secret and remove it safely.

## Rules of engagement
- Work only with the local training files in this mission.
- AI assistance is allowed and expected where useful.
- AI output is not evidence.
- Preserve objective verification evidence.
- Complete `ai_work_record.json`.

## Deliverables
- config.json references APP_API_KEY instead of a literal key
- no training secret remains in config.json
- .env.example documents APP_API_KEY without a value
- completed ai_work_record.json

## Finish
Run `range verify 1 <workspace>`. Technical completion is determined by the verifier, not by AI confidence.
