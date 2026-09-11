# Mission 8: Print Is Not a Log

**Phase:** B  
**Core skill:** Observability / evidence  

## Situation
A service prints human-readable activity to stdout but cannot reliably reconstruct who did what later.

## Objective
Configure structured security events with durable storage and actor/action/outcome fields.

## AI context
The learner distinguishes plausible AI explanations and console output from evidence suitable for investigation.

## Rules of engagement
- Work only with the local training files in this mission.
- AI assistance is allowed and expected where useful.
- AI output is not evidence.
- Preserve objective verification evidence.
- Complete `ai_work_record.json`.

## Deliverables
- logging.json uses structured format
- durable sink configured
- actor/action/outcome fields present
- completed ai_work_record.json

## Finish
Run `range verify 8 <workspace>`. Technical completion is determined by the verifier, not by AI confidence.
