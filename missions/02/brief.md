# Mission 2: Who Can Sudo

**Phase:** A  
**Core skill:** Privilege / permissions  

## Situation
A support analyst was granted broad sudo access during an incident. AI says the account is low risk because it is not an administrator account.

## Objective
Reduce sudo authority to the minimum command needed for log review and document why account labels do not establish privilege.

## AI context
AI provides an incomplete privilege assessment based on username/account role rather than effective sudo rights.

## Rules of engagement
- Work only with the local training files in this mission.
- AI assistance is allowed and expected where useful.
- AI output is not evidence.
- Preserve objective verification evidence.
- Complete `ai_work_record.json`.

## Deliverables
- sudoers.conf limits analyst to journalctl
- completed ai_work_record.json

## Finish
Run `range verify 2 <workspace>`. Technical completion is determined by the verifier, not by AI confidence.
