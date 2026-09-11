# Mission 12: Agent Gets a Tool

**Phase:** C  
**Core skill:** Agent / MCP / tool security  

## Situation
An assistant is connected to a tool catalog containing broad shell and file-system capabilities even though the business task only needs read-only knowledge access.

## Objective
Reduce the catalog to approved read-only tools, enforce default deny, and require confirmation for any future write action.

## AI context
The learner secures tool identity, authorization, and failure behavior instead of assuming the model will choose safe tools.

## Rules of engagement
- Work only with the local training files in this mission.
- AI assistance is allowed and expected where useful.
- AI output is not evidence.
- Preserve objective verification evidence.
- Complete `ai_work_record.json`.

## Deliverables
- tool_policy.json only allows kb.search and ticket.read
- default deny enabled
- write confirmation required
- completed ai_work_record.json

## Finish
Run `range verify 12 <workspace>`. Technical completion is determined by the verifier, not by AI confidence.
