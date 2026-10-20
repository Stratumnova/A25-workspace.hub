# A25 Terminal — Component Onboarding

**Owner / project lead:** Zed
**Status:** Owner-approved component plan and location; formal approval ticket filed; initial source committed but not certified
**Sources:** [Approved plan](APPROVED-BUILD-PLAN-V1.md), [original proposal](../build-requests/A25-TERMINAL-CONTROL-TOOLKIT-WORKSHOP-BUILD-REQUEST-DRAFT.md), [Node 11 charter](../../../../README.md)

## Start here
Read the Node 11 charter, parent Systems Hub README, this component README, approved plan and original proposal. Consult the latest real Office assignment before executing anything. Zed leads this component directly with one builder continuing from historical terminal stages. The builder's actual identity and current assignment must come from a later explicit record; never infer authority from historical material.

## Work stays here
Design, code, tests, repair, evidence, release ZIPs and recovery remain under `A25terminal/`. Add proposed `src/`, `tests/`, `fixtures/`, `docs/`, and `releases/` only when required by authorized implementation. Integrate separately through sibling `main build/` after verification; do not move the component.

## Team exchange and boundaries
- [Project lead](project-lead/README.md): Zed's scope, decisions and handoff.
- [Builder inbox](builders/inbox/README.md) / [outbox](builders/outbox/README.md): authorized work and observed results.
- [Archives inbox](archives/inbox/README.md) / [outbox](archives/outbox/README.md): indexing, provenance, custody and recovery.
- [Security inbox](security/inbox/README.md) / [outbox](security/outbox/README.md): identity, command gateway, network exposure, process safety, audit and secrets review.

Office keeps formal work orders, approval tickets and official responses; this project retains substantive build evidence. Do not edit another team's records without permission. Preserve original evidence and distinguish REFERENCE, HISTORICAL CLAIM, VERIFIED, ADOPTED, SUPERSEDED and UNKNOWN.

## Approved behavior and guardrails
Owner instructs GPT/Claude through existing interfaces. General legitimate owner-directed shell, files, sessions, lifecycle, backup and recovery capabilities are the design objective, not a four-command allowlist. GPT and Claude must have distinct authenticated principals. Future bots require separate scoped grants. No independent autonomous initiation, scheduling or API-triggered automatic work. Require real receipts, explicit high-impact confirmation, and recovery independent of the network connection. Security review precedes exposure.

## Not yet established
No new toolkit implementation, authenticated gateway, passing tests, live operation or integration is certified by these documents. Existing terminal plugins and older builds are evidence to investigate, not automatically adopted code. Do not touch the phone, tunnels, packages, services or historical repositories without separately authorized scope. No secrets or sensitive topology in public GitHub.

## Current owner addendum and next pass
Read [Owner Requirements — Test Boundary and Lockdown](project-lead/OWNER-REQUIREMENTS-2026-10-20-TEST-BOUNDARY-AND-LOCKDOWN.md) before testing or designing new controls. The owner supplied one exact authorized Android test directory and requires tests of the new controls, not merely the historical terminal transport. Password lockdown is a newly adopted design requirement, not an implemented or certified protection. [Approval Ticket 001](APPROVAL-TICKET-001.md) is now filed. Continue with scoped builder work and applicable Security review, recording actual author, time source, scope, execution and observed results.
