# A25 Chatroom — Workshop Team Lead Handoff

**Owner:** Zed  
**Seat:** A25-TW-GPT01, Workshop Lead  
**State:** Stage 0 CP0 accepted; Stage 1 M1 accepted for isolated sandbox engine; Stage 2 implementation on hold pending Security review.

## Start here

- [Durable Stage 0–1 memory and test ledger](A25-CHATROOM-WK-MEMORY-STAGE0-STAGE1-20261020.md)
- [Owner-approved scope](../APPROVED-BUILD-PLAN-V1.md)
- [Build stage plan](A25-CHATROOM-WK-WO-20261020T043822Z.md)
- [M1 acceptance](A25-CHATROOM-WK-ER-20261020T051100Z.md)
- [Seven-test full receipt](../builders/outbox/A25-CHATROOM-BD-RR-20261020T050733Z-M1-FINAL.md)

## Lead operating instructions

The Workshop Lead organizes, delegates, reviews evidence, preserves project history and makes checkpoint decisions. Builders perform implementation.

Use the established directories:

- `builders/inbox/` — builder assignments.
- `builders/outbox/` — implementation and test reports.
- `security/inbox/` and `security/outbox/` — Security requests and findings.
- `archives/inbox/` and `archives/outbox/` — Archives requests and findings.
- `project-lead/` — durable lead memory, stage recaps and recovery records.

Formal Office authority remains separate.

All work stays in:

**Repository:** `Stratumnova/A25-workspace.hub`

**Branch:** `main`

**Project:** `A25-node1125_hub/A25.archives/projects/a25-systems-hub/A25chatroom/`

No new repositories or branches, phone changes, live server operations, tunnel modifications, deployments or paid model APIs without separate owner authorization.

Do not publish secrets or owner-private operational findings.

## Milestone gates

| Gate | Status | Requirement |
|---|---|---|
| CP0 | ACCEPTED | Architecture reconnaissance |
| M1 | ACCEPTED — sandbox only | Seven committed tests passed per byte-verified builder receipt |
| M2 | PENDING | Security identity/permissions findings, implementation and negative tests |
| M3 | NOT STARTED | ZIP import/export, preservation and duplicate protection |
| M4 | NOT STARTED | Real user-invoked Zed/GPT/Claude interfaces |
| M5 | NOT STARTED | Reliability, recovery, physical and operational acceptance |

## Immediate next action

Have Security respond to the [existing identity-seam review request](../security/inbox/A25-CHATROOM-WK-IR-20261020T044600Z-SEC.md).

Security reports findings in `security/outbox/`.

Review mandatory controls before issuing the scoped Stage 2 implementation order.

Stage 2 must establish:

- Authenticated principal attribution independent of message content.
- Prevention of GPT/Claude deleting or clearing messages.
- Owner-only clearing after verified archive.
- Negative tests proving unauthorized actions fail.
- No network exposure without separate Security approval.

The Stage 1 Actor object is an injected testing interface, not production authentication.

## Evidence and owner rules

Distinguish REFERENCE, HISTORICAL CLAIM, VERIFIED, ADOPTED, SUPERSEDED and UNKNOWN.

A builder's test report is evidence of what the builder recorded; independent lead verification must be identified separately.

A sandbox PASS does not count as physical or operational verification.

Preserve failed reports, conflicting findings and chronology uncertainties.

At each milestone, publish a new linked recap without rewriting earlier evidence.

Use one meaningful build/test cycle per stage, with further correction only for demonstrated defects.

## Blocked GitHub or terminal operation

**STOP and inform Zed.**

Report what failed, where, and why. Obtain explicit approval before an identical retry.

Do not silently change method, target, inputs or scope.

Include this instruction in every builder-facing assignment.

## Stage 1 evidence index

The [durable Stage 0–1 memory](A25-CHATROOM-WK-MEMORY-STAGE0-STAGE1-20261020.md) records every test, its purpose, failure history, results and original source links.

Primary evidence:

- [Initial six-test run and independent probes](../builders/outbox/A25-CHATROOM-BD-RR-20261020T045156Z-M1-RETRY.md)
- [Corrected seven-test run](../builders/outbox/A25-CHATROOM-BD-RR-20261020T050733Z-M1-FINAL.md)

Verified implementation commit: `1de61b9926819c6b8173a4d839cb248b1b1715bb`

GitHub Actions was not the source of these test receipts.