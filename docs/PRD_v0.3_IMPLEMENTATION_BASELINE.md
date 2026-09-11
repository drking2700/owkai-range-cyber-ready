# OPERATION: CYBER READY — THE RANGE
## Product Requirements Document (PRD)
**Version:** 0.3  
**Date:** September 10, 2026  
**Status:** ACTIVE — V1 Built / Human Validation & Gate 2 Pending  
**Product Owner / Final Approver:** Donald King  
**Builder:** Codex  
**Independent Reviewer:** Claude

---

## 1. Product Summary

Operation: Cyber Ready — The Range is a free, mission-based, **AI-native cybersecurity training range** designed primarily for veterans and career-transition learners with little or no prior technical background.

The Range prepares learners for the cybersecurity workforce that now exists: one in which AI assists practitioners, AI is embedded in the systems being defended, and attackers increasingly use automation and AI to increase speed and scale.

The Range is not an LMS. Learners perform real security work against sanitized, production-inspired systems, use AI as a normal work tool, independently verify material conclusions, complete automated technical verification, participate in AI-coached after-action reviews (AARs), and leave with a reviewed portfolio demonstrating practical capability and accountable AI use.

The Range is the pre-apprenticeship/on-ramp into the broader Operation: Cyber Ready program.

## 2. Problem

Entry-level cyber programs often teach concepts without producing credible evidence that learners can perform real work. Common gaps include lecture-heavy content, unrealistic labs, certification-first learning, weak reasoning feedback, no employer-facing portfolio, expensive cloud labs, and assumptions of prior technical knowledge.

A second gap is now equally important: many programs still prepare learners for a pre-AI operating model. They either prohibit AI, ignore it, or isolate it into a late-stage module instead of teaching learners how to work safely and effectively in an AI-mediated security environment.

The Range must produce evidence that learners can perform applied cybersecurity work **with AI present** without allowing AI output to substitute for judgment, authorization, testing, or evidence. It must do so without exposing learners to production systems or creating meaningful recurring infrastructure cost.

## 3. Product Vision

A learner with no technical background should be able to enter the Range and develop into an **AI-native junior security practitioner**.

The learner should complete progressively harder real-world security missions, use AI to accelerate research and analysis, identify when AI output is incomplete or wrong, independently verify material conclusions, secure AI-enabled systems, explain risk clearly, receive structured feedback, and leave with credible evidence of practical capability.

The experience should feel closer to supervised junior security work in a modern AI-enabled organization than to a classroom.

## 4. North Star Outcome

A learner completes the program with:

- 16 completed missions.
- Passing automated verification for each mission.
- 16 AAR transcripts.
- Last four AARs scoring at least 4/5.
- Demonstrated ability to use AI for research, analysis, scripting, investigation, and communication without treating model output as authoritative evidence.
- Demonstrated ability to detect, challenge, and correct materially wrong or incomplete AI output.
- Demonstrated ability to secure systems containing AI/agent capabilities.
- A written governance/security assessment reviewed by a human.
- A completed 30-minute mock interview.
- A reviewed portfolio containing mission PRs, findings, verification evidence, AI-use records, AAR evidence, and capstone work.

## 5. Target Users

### Primary Learner
Veteran or career-transition learner, approximately 25–45, with little or no prior IT experience, able to commit roughly 8–10 hours/week, and seeking entry into cybersecurity / AI security.

### Secondary Learner
Existing Operation: Cyber Ready participants who need a practical range for applied learning.

### Reviewer / Instructor
Donald King, Jerry Butler / RTI where available, and future qualified reviewers/fellows.

## 6. Product Principles

1. **AI-native, human-accountable.** AI is a normal part of the workflow; the learner remains responsible for every material conclusion and action.
2. **AI may assist; AI may not be the authority.** Model output is not proof that a system is secure, a control works, a finding is valid, or an action is authorized.
3. **Evidence over model confidence.** Learners must verify through source inspection, testing, logs, configuration, reproducible checks, or other objective evidence.
4. Real over simulated.
5. Automated verification declares technical completion.
6. AAR is required after each mission.
7. Learners explain reasoning, not just provide answers.
8. Security fundamentals remain mandatory even when AI can generate commands, scripts, or explanations.
9. AI-security concepts appear throughout the curriculum rather than being isolated to a late module.
10. External resources teach fundamentals; the Range provides practice.
11. Military structure may inform framing, but civilian vocabulary remains primary.
12. Learner data is treated as PII.
13. Learners receive zero production access.
14. Near-zero operating cost is a design constraint.
15. Nothing is called successful unless a measurable artifact proves it.
16. Design freezes before broad implementation.
17. Keep the system simpler than the problem it solves.

## 7. Explicit Non-Goals

The Range will not be an LMS, video-course platform, certification-prep product, live production cloud lab, gamification platform, custom identity provider, mobile-first app, production ASCEND environment, or high-cost persistent cloud platform.

It will also not be a prompt-engineering bootcamp, a vendor-specific AI certification program, an AI-only curriculum that skips security fundamentals, or a system where learners can submit unverified model output as their work.

## 8. Program Structure

**Duration:** 16 weeks  
**Expected effort:** 8–10 hours/week  
**Weekly cadence:** prerequisite learning → mission brief → mission execution → automated verification → PR/evidence submission → AI-coached AAR → 60-minute cohort call.

### Phase A — Foundations (Weeks 1–4)

| Week | Mission | Core Security Skill | AI-Native Dimension |
|---|---|---|---|
| 1 | Plaintext | Secrets / data exposure | AI identifies possible secret exposure; learner must independently verify what is actually exposed and why it matters. |
| 2 | Who Can Sudo | Privilege / permissions | Learner evaluates an AI-generated privilege assessment that is incomplete or partially wrong. |
| 3 | Open Door | Network exposure | AI assists enumeration; learner must prove which exposure is real and distinguish hypothesis from evidence. |
| 4 | Git Remembers | Git history / secret leakage | Learner investigates AI-generated or AI-assisted code that leaves sensitive material in repository history. |

### Phase B — Guided Security Work (Weeks 5–8)

| Week | Mission | Core Security Skill | AI-Native Dimension |
|---|---|---|---|
| 5 | Rate the Limit | API abuse / rate limiting | Automated or agentic client generates machine-speed request volume; learner designs and verifies controls. |
| 6 | Silent Enum | Enumeration / discovery | Learner investigates automated/agentic reconnaissance and distinguishes normal automation from abuse. |
| 7 | Around the Log | Logging / telemetry gaps | Agent/tool activity occurs outside expected telemetry; learner determines what cannot be reconstructed. |
| 8 | Print Is Not a Log | Observability / evidence | Learner must distinguish AI explanation or console output from durable security evidence. |

**Week 8:** Human review.

### Phase C — Real Findings (Weeks 9–12)

| Week | Mission | Core Security Skill | AI-Native Dimension |
|---|---|---|---|
| 9 | Blast Radius | IAM / least privilege | AI agent receives excessive authority; learner measures blast radius and constrains permissions. |
| 10 | Tenant Walls | Isolation / multi-tenancy | AI-enabled workflow crosses a tenant or trust boundary; learner proves whether isolation failed. |
| 11 | Chain of Custody | Evidence / integrity | Learner evaluates whether AI-generated analysis is trustworthy and preserves verifiable evidence. |
| 12 | Agent Gets a Tool | Agent / MCP / tool security | Learner secures tool access, authorization, identity, and failure behavior for an AI agent. |

**Week 12:** Human review.

### Phase D — Capstone / Interview (Weeks 13–16)

| Week | Mission | Core Security Skill | AI-Native Dimension |
|---|---|---|---|
| 13 | Assessment Draft | Security assessment | Learner uses AI to accelerate assessment creation but must cite and verify every material claim. |
| 14 | AI as Analyst | AI-assisted investigation | Learner deliberately uses AI as an analyst, compares model output to evidence, and documents accepted/rejected reasoning. |
| 15 | Revise and Present | Communication / remediation | Learner critiques AI-generated recommendations, improves them, and presents a defensible final position. |
| 16 | Mock Interview | Employability / judgment | Learner explains where AI helped, where it failed, what required human judgment, and how evidence was established. |

**Week 16:** Final human review.

## 9. Mission Anatomy

Every mission must contain:

- **Prerequisite:** external learning, target ≤2 hours.
- **Brief:** maximum one page.
- **Objective:** falsifiable definition of done.
- **Environment:** pinned devcontainer / reproducible local environment; no production credentials or production network path.
- **AI Context:** explicit description of how AI is present in the mission—as practitioner assistant, system component, attacker automation, or combination.
- **Execute:** real work; AI assistance is allowed/expected where appropriate; hints only after meaningful attempt (target: 20 minutes).
- **AI Work Record:** concise record of what the learner asked AI to do, which outputs were accepted/rejected, and how material conclusions were verified. Full prompt transcripts are not required unless the mission specifically needs them.
- **Verification:** pytest, shell, static linting, Parliament, ruff, custom rules, and/or direct evidence inspection. Model output alone never satisfies verification.
- **Deliverable:** pull request using standard template with evidence.
- **AAR:** 15–25 minute AI-coached review scored 0–5 across Accuracy, Risk reasoning, Fix justification, Verification, and Communication, including whether AI assistance was used responsibly.

## 10. AI Operating Doctrine

Every learner is taught the same operating doctrine from Week 1.

### USE AI TO
- Accelerate research.
- Explain unfamiliar code or configurations.
- Generate investigation hypotheses.
- Draft scripts and queries.
- Compare policies/configurations.
- Summarize vulnerabilities and logs.
- Generate threat scenarios.
- Draft findings and executive explanations.
- Challenge the learner's own assumptions.

### NEVER TREAT AI AS AUTHORITY TO
- Declare a system secure.
- Approve production.
- Establish that a control works.
- Determine authorization.
- Establish evidence.
- Make an unverified material risk decision.
- Replace the learner's responsibility for submitted work.

### ALWAYS
- Verify material claims.
- Test the result.
- Inspect source/configuration/evidence where available.
- Preserve evidence.
- Understand what context the model received.
- Understand which tools/actions the model could invoke.
- Identify who authorized consequential actions.
- Document when AI output was rejected or corrected.

The product must reward good judgment, not prompt fluency.

## 11. Core Components

### C1 — Mission Content Repository
Public GitHub repo `owkai-range-content` with mission briefs, prerequisites, templates, verification rules, and devcontainer definitions.

### C2 — Range Devcontainers
Pinned images by phase; GitHub Codespaces compatible; local Docker fallback; no embedded production credentials.

### C3 — Verification Harness
pytest / shell / lint / Parliament / ruff / custom checks, running in learner CI.

### C4 — AI Assistance & AAR Layer
Provides two bounded functions:

1. **Learner AI Assistant:** tool-agnostic AI assistance for research, analysis, scripting, investigation, and drafting. Usage is capped and designed for low cost. The assistant may help reason but cannot satisfy mission verification by itself.
2. **AAR Coach:** AI-driven structured interview, transcript creation, rubric scoring, learner token/cost cap, and static fallback prompts if the model is unavailable.

The vertical slice must measure combined learner-assistant + AAR cost before external pilot.

### C5 — Learner Portal
Minimal portal for GitHub login, mission list, launch, AAR, and progress.

### C6 — Progress & Evidence
Learner repository is the primary system of record; minimal index stores learner ID, mission completion, score, and review status.

### C7 — Reviewer Console
Review learner progress, checkpoint evidence, human assessments, and completion.

## 12. Security / Privacy Requirements

### Zero Production Surface
Learners must never receive production credentials, secrets, network access, databases, or customer data.

### Sanitized Training Fork
Before learner use: secret scan complete, sensitive identifiers removed, production endpoints removed, Git history reviewed, and snapshot approved through Gate 1.

### Learner Data
Repositories private by default; veteran identification optional; minimum PII; consent captured at enrollment; portal stores scores/status only where possible; AAR provider retention terms verified before pilot.

### AI Security
Prompt-injection test harness required before external pilot. AI assistance and the AAR coach must not expose hidden prompts, secrets, other learner data, or unauthorized tools.

Learner AI access must:
- Use no production credentials.
- Have no production network path.
- Operate under explicit tool/permission boundaries.
- Be cost-capped.
- Have documented provider retention/privacy behavior.
- Avoid treating model output as authoritative completion evidence.

## 13. Cost Requirements

Primary target: **< $50 total infrastructure/model cost per 8-person 16-week cohort**, excluding human labor.

AAR target: approximately $0.10–$0.40 per completed AAR where achievable. The **combined learner AI assistance + AAR cost** must be measured during the vertical slice and remain compatible with the cohort cost ceiling. Prefer GitHub free/public infrastructure, local execution, small/efficient models where appropriate, static/reproducible environments, strict token caps, and minimal persistent backend.

## 14. Functional Requirements

| ID | Requirement | Priority | Status |
|---|---|---:|---|
| FR-001 | Learner can access mission content | P0 | NOT STARTED |
| FR-002 | Learner can launch pinned mission environment | P0 | NOT STARTED |
| FR-003 | Learner can execute mission locally/Codespaces | P0 | NOT STARTED |
| FR-004 | Automated verifier returns deterministic pass/fail | P0 | NOT STARTED |
| FR-005 | Learner submits work through PR | P0 | NOT STARTED |
| FR-006 | AI coach conducts mission AAR | P0 | NOT STARTED |
| FR-007 | AAR rubric score is recorded | P0 | NOT STARTED |
| FR-008 | Learner progress is visible | P1 | NOT STARTED |
| FR-009 | Human reviewer can review checkpoints | P1 | NOT STARTED |
| FR-010 | Learner can complete Missions 1, 5, 9 vertical slice | P0 | NOT STARTED |
| FR-011 | Learner data remains private by default | P0 | NOT STARTED |
| FR-012 | Sanitized assets contain no production secrets | P0 | NOT STARTED |
| FR-013 | Mission verification runs in CI | P0 | NOT STARTED |
| FR-014 | AAR failure has manual fallback | P1 | NOT STARTED |
| FR-015 | Learner can retain portfolio evidence | P1 | NOT STARTED |
| FR-016 | Learner has an approved AI-assistance path during missions | P0 | NOT STARTED |
| FR-017 | Learner records material AI assistance and verification decisions | P0 | NOT STARTED |
| FR-018 | No mission can be passed using model output without objective verification | P0 | NOT STARTED |
| FR-019 | Every mission contains an explicit AI-native dimension | P0 | IN DESIGN |
| FR-020 | Learner encounters intentionally incomplete/wrong AI output and demonstrates correction | P0 | NOT STARTED |
| FR-021 | Portfolio demonstrates AI-assisted work plus independent evidence and human accountability | P1 | NOT STARTED |

## 15. Non-Functional Requirements

| ID | Requirement | Target |
|---|---|---|
| NFR-001 | Cohort infrastructure/model cost | < $50 / 8 learners / 16 weeks |
| NFR-002 | Production access | Zero |
| NFR-003 | Environment reproducibility | Pinned/versioned |
| NFR-004 | Verification reliability | Deterministic for known solution |
| NFR-005 | Secret exposure | Zero known secrets |
| NFR-006 | Environment startup | Practical for novice learner |
| NFR-007 | AAR duration | 15–25 minutes |
| NFR-008 | Learner weekly effort | ~8–10 hours |
| NFR-009 | Mission brief length | ≤1 page |
| NFR-010 | System complexity | Minimum required for learner outcome |
| NFR-011 | AI-provider dependency | Tool/provider agnostic where practical |
| NFR-012 | AI-assistance cost | Bounded within total cohort cost target |
| NFR-013 | AI evidence standard | Model output never counts as sole verification |
| NFR-014 | AI data retention | Documented and acceptable before pilot |

## 16. Quality Gates

### Gate 1 — Design / Training Asset Approval
Required before external build/use:
- PRD approved.
- Source-of-truth documents reconciled.
- AI Operating Doctrine approved.
- All 16 missions have an approved AI-native dimension.
- Missions 1, 5, 9 specified in implementation detail.
- Missions 1, 5, 9 each require AI assistance plus independent verification.
- Sanitized training snapshot complete.
- Credential remediation evidence complete.
- Environment design approved.
- Verification approach approved.
- Learner AI-assistance access model approved.
- AI Work Record format approved.
- AAR rubric approved.
- Combined learner-AI + AAR cost model defined.
- AI provider retention/privacy terms evaluated.
- Privacy/consent plan drafted.

**Approver:** Donald King

### Gate 2 — Vertical Slice Approval
Required before external pilot. Three test learners must complete Mission 1 → Mission 5 → Mission 9 with working environments, approved AI assistance, automated verification, PR evidence, AI Work Records, AAR transcripts/scores, measured cost, zero production access, zero credential leakage, and at least one nontechnical learner completing the flow.

At least one vertical-slice mission must intentionally provide materially incomplete or wrong AI output and require the learner to detect, reject/correct, and independently verify the result.

**Approver:** Donald King

## 17. Build Roadmap

### Phase 0 — Design Freeze
Deliver PRD v1.0, source reconciliation, AI Operating Doctrine, approved AI-native mapping for all 16 missions, architecture rulings, detailed AI-native Missions 1/5/9, learner AI-assistance model, sanitization plan, and Gate 1 package.

**Exit:** GATE 1 APPROVED

### Phase 1 — Vertical Slice
Build C2/C3/C4/minimal C5, AI-native Missions 1/5/9, and sanitized training fork. Run technical and nontechnical dry runs, including AI-assisted analysis, intentionally flawed AI output, independent verification, and AAR review.

**Exit:** GATE 2 APPROVED

### Phase 2 — Philadelphia Pilot
Proposed: 5 learners, Missions 1–4, previews of 5 and 9 as appropriate, weekly live call, human checkpoint review.

Measure completion, time/mission, hint use, AAR trajectory, cost/learner, dropout, technical failures, and learner ability to explain findings cold.

### Phase 3 — Full Build
Build Missions 5–16, reviewer console, consent/privacy workflows, portfolio completion flow, and full cohort.

### Phase 4 — Sustain
Repeat cohorts, improve curriculum from measured outcomes, enable graduate contribution, and pursue apprenticeship/grant/veteran-program pathways where validated.

## 18. Success Metrics

### Learner Outcome
Mission completion, verification pass rate, AAR progression, last 4 AARs ≥4/5, capstone completion, mock interview pass, portfolio completion, responsible AI-use quality, ability to detect/correct wrong AI output, and ability to distinguish hypothesis/model output from verified security evidence.

### Product Quality
Environment launch success, verifier accuracy, AAR scoring consistency, secret leakage incidents, support burden, and cost per learner.

### Pilot Questions
1. Can a nontechnical learner use the environment?
2. Can learners progress without instructor hand-holding?
3. Does automated verification reliably identify completion?
4. Does the AAR improve reasoning and communication?
5. Is the program affordable enough to sustain?
6. Can reviewers identify real skill progression?
7. Do learners leave with credible work artifacts?
8. Can learners use AI to accelerate work without accepting unverified conclusions?
9. Can learners detect and correct intentionally flawed AI analysis?
10. Can learners explain where AI helped, where it failed, and what required human judgment?

## 19. Team / Decision Rights

### Product Owner / Final Approver — Donald King
Product decisions, gate approvals, scope decisions, and strategic partner decisions.

### Builder — Codex
Implementation, tests, devcontainers, verification harness, portal/integration code, and technical documentation.

### Independent Reviewer — Claude
Adversarial review, requirements conformance, security review, test-gap identification, and seeded defect review.

**Rule:** Builder and reviewer remain separate model surfaces.

## 20. Work Tracker

### P0 — Immediate
| ID | Work Item | Owner | Status | Exit Evidence |
|---|---|---|---|---|
| OCR-001 | Approve PRD v0.2 AI-native direction | Donald | IN REVIEW | Approval |
| OCR-002 | Reconcile authoritative design sources | Donald / Reviewer | NOT STARTED | Source register |
| OCR-003 | Define AI-native Mission 1 in implementation detail | Codex | NOT STARTED | Mission spec |
| OCR-004 | Define AI-native Mission 5 in implementation detail | Codex | NOT STARTED | Mission spec |
| OCR-005 | Define AI-native Mission 9 in implementation detail | Codex | NOT STARTED | Mission spec |
| OCR-006 | Create sanitized training snapshot plan | Codex | NOT STARTED | Sanitization plan |
| OCR-007 | Execute credential/secret scan | Codex | NOT STARTED | Scan evidence |
| OCR-008 | Define devcontainer baseline | Codex | NOT STARTED | Working container |
| OCR-009 | Define verifier contract | Codex | NOT STARTED | Test specification |
| OCR-010 | Define AI-aware AAR rubric + response schema | Donald / Claude | NOT STARTED | Approved rubric |
| OCR-011 | Measure combined learner-AI + AAR cost assumptions | Codex | NOT STARTED | Cost test |
| OCR-012 | Assemble Gate 1 package | Codex | NOT STARTED | Gate package |
| OCR-013 | Independent Gate 1 review | Claude | NOT STARTED | Review findings |
| OCR-014 | Gate 1 decision | Donald | BLOCKED | APPROVE / REJECT |
| OCR-015 | Finalize AI Operating Doctrine | Donald / Claude | IN DESIGN | Approved doctrine |
| OCR-016 | Define learner AI-assistance access, permission, privacy, and cost model | Codex / Claude | NOT STARTED | AI access design |
| OCR-017 | Define AI Work Record schema | Codex | NOT STARTED | Evidence schema |
| OCR-018 | Define AI-verification rubric / evidence standard | Donald / Claude | NOT STARTED | Approved verification standard |
| OCR-019 | Approve AI-native dimension for all 16 missions | Donald / Claude | IN DESIGN | Curriculum mapping |

### P1 — After Gate 1
| ID | Work Item | Owner | Status |
|---|---|---|---|
| OCR-101 | Build AI-native Mission 1 vertical slice | Codex | BLOCKED |
| OCR-102 | Build AI-native Mission 5 vertical slice | Codex | BLOCKED |
| OCR-103 | Build AI-native Mission 9 vertical slice | Codex | BLOCKED |
| OCR-104 | Build minimal learner flow | Codex | BLOCKED |
| OCR-105 | Integrate AAR coach | Codex | BLOCKED |
| OCR-106 | Configure CI verification | Codex | BLOCKED |
| OCR-107 | Internal technical dry run | Donald | BLOCKED |
| OCR-108 | Internal nontechnical dry run | TBD | BLOCKED |
| OCR-109 | Independent vertical-slice review | Claude | BLOCKED |
| OCR-110 | Gate 2 decision | Donald | BLOCKED |

## 21. Open Issues / Decisions

| ID | Question | Status |
|---|---|---|
| OI-001 | Final AAR model/provider | OPEN |
| OI-002 | AAR provider retention/privacy terms | OPEN |
| OI-003 | Exact learner identity/login flow | OPEN |
| OI-004 | Exact repository ownership/provisioning flow | OPEN |
| OI-005 | Final sanitized ASCEND snapshot scope | OPEN |
| OI-006 | Philadelphia OVA pilot confirmation | OPEN |
| OI-007 | Pilot learner recruitment method | OPEN |
| OI-008 | PA apprenticeship/grant eligibility | OPEN |
| OI-009 | VA/VET TEC compatibility/path | OPEN |
| OI-010 | January 2027 full-cohort feasibility | OPEN |
| OI-011 | Learner AI-assistance provider/model strategy | OPEN |
| OI-012 | Combined learner-AI + AAR cost ceiling allocation | OPEN |
| OI-013 | AI Work Record retention/privacy requirements | OPEN |
| OI-014 | Minimum AI fluency expected at graduation | OPEN |

Open issues do not automatically block Phase 0 unless they prevent Gate 1 evidence.

## 22. Change Control

Any proposed change affecting the 16-week structure, AI-native/human-accountable doctrine, zero-production-access rule, near-zero-cost requirement, required AAR, automated verification, learner AI-assistance model, learner evidence model, builder/reviewer separation, product scope, or pilot scope must be recorded as a PRD decision/change.

Every material change requires:
1. Problem/evidence.
2. Proposed change.
3. Impact.
4. Tradeoff.
5. Donald's ruling.

No major architecture or product change occurs solely because a model suggests a better design.

## 23. Change Log

### v0.2 — September 10, 2026
**Decision:** Redesign the Range from a traditional cybersecurity curriculum with late AI content into an **AI-native, human-accountable cybersecurity range**.

Material changes:
- Learner identity changed to AI-native junior security practitioner.
- AI is present from Mission 1 onward.
- Security fundamentals remain mandatory.
- AI output cannot satisfy verification by itself.
- Every mission now has an explicit AI-native dimension.
- Added AI Operating Doctrine.
- Added AI Work Record requirement.
- Expanded C4 into learner AI assistance + AAR.
- Added requirements for detecting/correcting flawed AI output.
- Added Gate 1/Gate 2 evidence for AI usage, verification, privacy, and cost.
- Added AI-native work items and open issues.

This change occurred before implementation and is therefore treated as product-design correction, not scope creep.

## 24. Current Product Status

**Overall:** V1 CODEBASE BUILT — HUMAN VALIDATION / GATE 2 PENDING

**Completed:** product purpose, target learner, 16-mission curriculum structure, AI-native learner identity, AI Operating Doctrine draft, mission-level AI mapping, mission anatomy, core architecture, safety/cost constraints, and builder/reviewer roles.

**In Progress:** independent review, technical/nontechnical human dry runs, AAR calibration, provider privacy review, and Gate 2 evidence collection.

**Next:**
1. Complete independent Claude review and resolve findings.
2. Run one technical human dry run.
3. Run one nontechnical human dry run.
4. Measure learner usability, time, hints, AAR quality, and cost.
5. Approve the selected external AI provider's retention/privacy posture if enabled.
6. Assemble Gate 2 evidence.
7. Donald issues formal Gate 2 APPROVE / REJECT decision before external pilot.

## 25. Definition of PRD v1.0

PRD becomes v1.0 when:
- Donald approves the AI-native product direction and scope.
- Known design contradictions are reconciled.
- AI Operating Doctrine is final.
- All 16 missions have approved AI-native dimensions.
- Missions 1, 5, and 9 have implementable AI-native specifications.
- Learner AI-assistance, privacy, cost, and evidence models are resolved.
- Gate 1 acceptance criteria are final.
- Architecture assumptions needed for vertical-slice implementation are resolved.

Until then, this document is the active tracking baseline.

---

# Implementation Addendum — v0.3 Baseline

**Date:** September 10, 2026  
**Implementation state:** V1 codebase built; human validation and formal Gate 2 approval pending.

The product owner directed implementation to begin after v0.2. The current repository now implements C1–C7 at V1 scope, all 16 missions, deterministic verification, AI Work Records, bounded AI assistance, AAR workflow, GitHub-OAuth-ready identity, progress/cost indexing, reviewer workflow, CI, secret scanning, sanitization tooling, and portfolio export.

Formal quality-gate status is maintained in `docs/GATE_STATUS.md`. The implementation does not waive independent-review, human dry-run, privacy-provider, or pilot approval requirements.
