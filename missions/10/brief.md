# Mission 10: Tenant Walls

**Phase:** C  
**Core skill:** Isolation / multi-tenancy  

## Situation
An AI-enabled workflow trusts a tenant identifier supplied in a request body instead of the authenticated identity.

## Objective
Bind tenant authorization to a trusted token claim and enforce a subject-resource tenant match.

## AI context
The learner secures an AI workflow crossing trust boundaries and proves tenant isolation rather than trusting application intent.

## Rules of engagement
- Work only with the local training files in this mission.
- AI assistance is allowed and expected where useful.
- AI output is not evidence.
- Preserve objective verification evidence.
- Complete `ai_work_record.json`.

## Deliverables
- authz.json uses token_claim tenant source
- tenant match enforcement enabled
- completed ai_work_record.json

## Finish
Run `range verify 10 <workspace>`. Technical completion is determined by the verifier, not by AI confidence.
