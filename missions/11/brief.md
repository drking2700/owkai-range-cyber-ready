# Mission 11: Chain of Custody

**Phase:** C  
**Core skill:** Evidence / integrity  

## Situation
An AI-generated incident summary references local artifacts but the evidence package has no integrity metadata.

## Objective
Create a verifiable evidence manifest with SHA-256 hashes, UTC timestamp, and tool version.

## AI context
The learner decides whether AI-generated analysis can be trusted by anchoring claims to preserved, hashed evidence.

## Rules of engagement
- Work only with the local training files in this mission.
- AI assistance is allowed and expected where useful.
- AI output is not evidence.
- Preserve objective verification evidence.
- Complete `ai_work_record.json`.

## Deliverables
- evidence_manifest.json includes hashes for event.log and config_snapshot.json
- UTC collected_at
- tool_version
- completed ai_work_record.json

## Finish
Run `range verify 11 <workspace>`. Technical completion is determined by the verifier, not by AI confidence.
