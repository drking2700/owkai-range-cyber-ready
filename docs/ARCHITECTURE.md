# V1 Architecture

## Principle
The learner repository/workspace is the primary evidence record. The portal is an index and workflow layer, not a learning-management system.

## Components

1. **Mission packages** — 16 versioned local training environments and deterministic verification rules.
2. **Range CLI** — bootstraps missions, runs verification, initializes demo state, and exports portfolio summaries.
3. **Learner portal** — mission discovery, bounded AI assistance, AAR entry point, and progress view.
4. **AI layer** — provider abstraction with local deterministic fallback and optional OpenAI-compatible endpoint. No model tool execution.
5. **AAR layer** — structured questions plus deterministic fallback scoring so the product works without a model provider.
6. **SQLite index** — learner identity, mission status, AAR scores, AI cost ledger, human checkpoint reviews.
7. **Reviewer console** — reads minimum indexed progress; learner artifacts remain in the learner workspace/repository.
8. **CI/security** — product tests and a training-secret scan.

## Trust boundaries

- No production data or production credentials.
- AI provider receives only learner-entered question + mission metadata in configured mode.
- AI output cannot mutate workspace files through this application.
- Verification reads local learner files and compares them to explicit rules.
- Human review is required at missions 8, 12, and 16.

## Deployment
V1 can run locally, in Codespaces, or as a single small container. Persistent backend requirements are only SQLite and the repository/workspace evidence source.
