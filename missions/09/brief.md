# Mission 9: Blast Radius

**Phase:** C  
**Core skill:** IAM / least privilege  

## Situation
An AI agent received a wildcard cloud policy so it could read one training evidence path. AI says the policy is acceptable because the environment is nonproduction.

## Objective
Replace wildcard authority with the minimum read permission for the required training object path.

## AI context
The agent has excessive authority. The learner measures blast radius and constrains action/resource scope.

## Rules of engagement
- Work only with the local training files in this mission.
- AI assistance is allowed and expected where useful.
- AI output is not evidence.
- Preserve objective verification evidence.
- Complete `ai_work_record.json`.

## Deliverables
- policy.json contains only s3:GetObject
- resource limited to arn:aws:s3:::training-evidence/mission9/*
- no wildcard actions/resources
- completed ai_work_record.json

## Finish
Run `range verify 9 <workspace>`. Technical completion is determined by the verifier, not by AI confidence.
