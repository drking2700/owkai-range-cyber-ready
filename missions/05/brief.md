# Mission 5: Rate the Limit

**Phase:** B  
**Core skill:** API abuse / rate limiting  

## Situation
An internal agent can call a business API as fast as it can generate requests. The endpoint currently has no rate control.

## Objective
Implement bounded per-identity request limits and a small burst allowance suitable for an automated client.

## AI context
An agentic client generates machine-speed traffic; the learner must design limits that preserve business use without allowing unbounded requests.

## Rules of engagement
- Work only with the local training files in this mission.
- AI assistance is allowed and expected where useful.
- AI output is not evidence.
- Preserve objective verification evidence.
- Complete `ai_work_record.json`.

## Deliverables
- api_policy.json enables per-identity rate limiting
- limit is <=60/minute
- burst is <=10
- completed ai_work_record.json

## Finish
Run `range verify 5 <workspace>`. Technical completion is determined by the verifier, not by AI confidence.
