# A25 Terminal — Owner-Approved Build Plan V1

**Owner and component lead:** Zed
**Status:** ADOPTED — component location and submitted Terminal Control Toolkit build plan approved; implementation not certified or ordered by this record
**Record:** APPROVED-BUILD-PLAN-V1.md (stable component decision record)
**Time source:** GitHub publication commit metadata; owner's approval expressed in this ChatGPT conversation on 2026-10-20
**Prepared by:** A25 Archives
**Original proposal:** [Workshop builder draft](../build-requests/A25-TERMINAL-CONTROL-TOOLKIT-WORKSHOP-BUILD-REQUEST-DRAFT.md)
**Parent:** [A25 Systems Hub](../README.md)

## Owner approval and scope

Zed explicitly approved the permanent sibling component `A25terminal/`, the submitted Terminal Control Toolkit build plan, and establishment of its documentation, onboarding and team exchange space. Zed is **Terminal Project Lead**, directing one builder brought forward from the historical terminal-build stages. This does not appoint a different Workshop lead to this component.

This approval adopts the plan's intended capability: GPT and Claude perform owner-requested terminal and file tasks through independently authenticated connections, including general shell operations, interactive sessions, service controls, backups, evidence and recovery. Three future bots may use role-scoped interfaces only after their own authorization. No autonomous initiation, scheduled work, or API-triggered independent tasks. Safeguards include actual caller identity, authorization, confirmation for high-impact actions, auditable outcomes and independent local recovery.

**Approval is not verification of implementation.** No code, package installation, service change, phone action, tunnel exposure, migration or deployment is authorized merely by creating these documents. The builder requires separately scoped instructions and Security review where relevant. The formal owner approval ticket will be added in a subsequent pass, as Zed directed.

## Approved permanent location and lanes

- `A25terminal/` — permanent source, tests, evidence, repairs, ZIP/recovery and handoff home.
- `project-lead/` — Zed's component lead records and decisions.
- `builders/inbox/` and `builders/outbox/` — one builder's scoped assignments and actual results.
- `archives/inbox/` and `archives/outbox/` — Archives custody and indexing.
- `security/inbox/` and `security/outbox/` — Security reviews and responses.
- `src/`, `tests/`, `fixtures/`, `docs/`, `releases/` — proposed functional directories, created only when actual implementation work requires them.
- Sibling `main build/` — approved integration after verification; never relocate component source.

## Evidence, restrictions and handoff

The [original builder draft](../build-requests/A25-TERMINAL-CONTROL-TOOLKIT-WORKSHOP-BUILD-REQUEST-DRAFT.md) is preserved without edits. Its heading still says PROPOSED because it is the historical original; this separate record governs the **adopted plan and location**. Prior Pocket Server/Gate/terminal implementations are REFERENCE until specifically examined and accepted; no implicit reuse or migration.

Owner decisions are ADOPTED. Local runtime, authenticated interfaces, tests and deployment remain UNKNOWN until supported by actual evidence. No secrets, endpoints, credentials or private logs in public GitHub. Work only in `Stratumnova/A25-workspace.hub` on `main`. Formal orders and approval ticket remain separate from this project decision record.
