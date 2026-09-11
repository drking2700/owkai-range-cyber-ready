# Mission 4: Git Remembers

**Phase:** A  
**Core skill:** Git history / secret leakage  

## Situation
A secret was removed from the current file, but a simulated repository-history extract still contains it.

## Objective
Document rotation/history-remediation actions and prove the exposed credential is revoked.

## AI context
AI-generated code caused a secret to be committed; the learner must reason about current-file cleanup versus historical exposure.

## Rules of engagement
- Work only with the local training files in this mission.
- AI assistance is allowed and expected where useful.
- AI output is not evidence.
- Preserve objective verification evidence.
- Complete `ai_work_record.json`.

## Deliverables
- revoked_secrets.json records revoked credential
- remediation.md explains rotation and history rewrite
- completed ai_work_record.json

## Finish
Run `range verify 4 <workspace>`. Technical completion is determined by the verifier, not by AI confidence.
