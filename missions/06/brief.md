# Mission 6: Silent Enum

**Phase:** B  
**Core skill:** Enumeration / discovery  

## Situation
Automated discovery requests blend into ordinary traffic because actor and request metadata are incomplete.

## Objective
Enable sufficient telemetry and thresholding to detect repeated enumeration by one identity.

## AI context
The learner distinguishes normal automation from suspicious automated discovery using evidence rather than request volume alone.

## Rules of engagement
- Work only with the local training files in this mission.
- AI assistance is allowed and expected where useful.
- AI output is not evidence.
- Preserve objective verification evidence.
- Complete `ai_work_record.json`.

## Deliverables
- telemetry.json records actor_id, user_agent, path, outcome
- enumeration threshold configured
- completed ai_work_record.json

## Finish
Run `range verify 6 <workspace>`. Technical completion is determined by the verifier, not by AI confidence.
