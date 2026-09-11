# Mission 7: Around the Log

**Phase:** B  
**Core skill:** Logging / telemetry gaps  

## Situation
A tool action can bypass the normal application request logger, leaving no durable audit event.

## Objective
Require auditable records for all tool actions and route them to an append-only sink.

## AI context
Agent/tool activity exposes an observability blind spot; the learner determines what cannot be reconstructed after the fact.

## Rules of engagement
- Work only with the local training files in this mission.
- AI assistance is allowed and expected where useful.
- AI output is not evidence.
- Preserve objective verification evidence.
- Complete `ai_work_record.json`.

## Deliverables
- audit_policy.json requires audit for all actions
- sink is append_only
- completed ai_work_record.json

## Finish
Run `range verify 7 <workspace>`. Technical completion is determined by the verifier, not by AI confidence.
