# Identity and Repository Model

## V1 decision

The Range does **not** build a custom identity provider.

- Local/dry-run mode uses a minimal learner identifier.
- Deployment mode can use GitHub OAuth via `/auth/github` when `GITHUB_CLIENT_ID` and `GITHUB_CLIENT_SECRET` are configured.
- OAuth access tokens are deliberately not persisted in V1.
- Learner-owned/private GitHub repositories remain the intended system of record for work, PRs, AI Work Records, AAR artifacts, and portfolio evidence.

Repository creation/provisioning is intentionally an operations step rather than a privileged portal feature in V1. This keeps the portal out of the business of storing long-lived GitHub write tokens and preserves the zero-trust/minimum-state design.
