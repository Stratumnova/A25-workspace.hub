# A25 Systems Hub — Request for Build-Order Authorization and Planning Intake

**Record ID:** A25-SYSTEMS-HUB-WK-WR-20261020T020916Z.md
**Created:** 2026-10-20 02:09:16 UTC
**Time source:** execution environment `date -u`
**Author / role:** A25-TW-GPT01, Workshop Lead
**From:** Workshop Lead on Zed's explicit request
**To:** Zed / authorized A25 Project leadership, Workshop Office
**Project:** A25 Systems Hub (official successor to the current Pocket Server)
**Document type:** WR — Work Request
**Status:** OPEN — REQUEST FOR AUTHORIZATION; NOT A BUILD ORDER
**Branch:** `main` in `Stratumnova/A25-workspace.hub`
**Owner direction:** Zed, Oct 19 2026, requested formal build-order request and Archives project setup.
**Canonical project home:** to be created/confirmed by Archives under `A25-node1125_hub/A25.archives/projects/`
**Related Archives setup request:** `A25.office/teams/archives/requests/incoming/A25-SYSTEMS-HUB-AG-WR-20261020T020916Z.md`

## Requested decision

Authorize a staged **planning and subsequent separately approved implementation** program for A25 Systems Hub using the established Workshop structure. Zed requests the build-order intake now, not immediate source edits, deployment, phone actions, branch creation, or tunnel changes. A properly scoped implementation work order must follow the applicable approvals and Security review.

## Purpose and replacement boundary

Build the official **A25 Systems Hub** to replace the existing Pocket Server / temporary **Workstation Roundtable 01** as the reusable, secure foundation for A25 AI workshop collaboration. Preserve the existing working environment as scaffolding/reference until a verified cutover, without inheriting its weaknesses or historical assumptions.

**Owner-specified cutoff:** 2026-10-19 **20:07 MDT** (2026-10-20 02:07 UTC). Anything built before that instant—including Gate-01, Gate-02, Shared Space, historical bridges, tunnels, code, old project orders and reports—is **historical reference, not automatically approved source, architecture, or implementation** for the official successor. Do not delete, rewrite, or silently migrate originals. Later records are not automatically verified or adopted either; they follow the new charter.

This is a project-direction and evidence classification boundary, **not** an assertion that the old Pocket Server was technically shut down at that time or that prior owner seals lost their scope.

## What to build, and why

1. **Persistent Message Hub (first functional milestone):** a chat-style place for Zed, GPT and Claude to type/paste, read and reply without dumping Markdown in tmux or couriering GitHub/Drive messages. Durable message IDs, timestamps, authorship, ordered delivery, restart recovery and auditability.
2. **Three collaborative conversation/work areas:** GPT-led, Claude-led, and Shared Roundtable. All three participants may review and contribute across all areas; the area marks who is leading a task, **not private or exclusive access**. Zed can participate in each.
3. **Independent identities and authenticated entryways:** unique credentials/tokens and verifiable caller identity for GPT, Claude and owner; server-enforced authorization for messaging and tools, token lifecycle and auditable attribution. Never rely on an AI's self-declared name.
4. **Local-first canonical working files:** Node 11 hub structure under planned `Documents/A25-node1125_hub/`; GitHub `main` is the temporary coordination/version-control and remote backup mirror, **not** the live message database. Archives must determine safe storage boundaries: readable project documents versus Termux-private secrets, runtime databases and sensitive configs.
5. **Independent server, bridges and tunnels:** A25 Systems Hub gets its own tested runtime and network configuration, not reuse of the exposed public bridge as production. Use existing workstation only as authorized scaffolding during construction.
6. **Controlled shared terminal/workshop capability:** both GPT and Claude may use appropriate terminal tools with distinct authenticated principals, scoped commands, logged actions, and owner-approved access. Separate message access from command execution and enforce least privilege.
7. **Reliable operations:** startup/shutdown, backup and restore tests, health checks, incident response, source provenance, staged deployment and rollback.
8. **Evidence-driven migration:** run the successor separately, independently test security and continuity, obtain Zed's cutover authorization, then retire the old bridge/tunnel. Never switch merely because the new code exists.

## Known information

- Current working prototype has demonstrated GPT terminal and tunnel connectivity, but historical security reviews reported missing application authentication and shared bridge identity. These are **reference/reported findings**, not certification of current runtime state.
- Owner selected A25 Systems Hub as official name and adopted Message Hub first, followed by local storage and full server capabilities.
- Existing hub repository `Stratumnova/A25-workspace.hub` and branch `main` are mandatory. No new repository, fork, branch, or separate workspace.
- Node 11 charter routes Office requests/orders/results separately from substantive Archives project history.
- Archives must create/maintain canonical project location; Workshop should link to it rather than duplicate the plan.

## Information needed before an implementation order

- Archives-confirmed canonical project path, initial README, source index and local-storage placement; how Git checkout and protected Termux runtime relate.
- Security-reviewed threat model, identity/credential design, terminal privilege boundaries and safe cutover/rollback plan.
- Message Hub minimal interface (owner chat UI versus terminal client), persistence engine, API contract, delivery semantics, retention and recovery.
- Exact builder seats, ownership and order dependencies; implementation/test environment and owner approval gates.
- Source inventory and per-component verification/adoption decisions; distinguish reference code from accepted code.
- Backup encryption, Git ignore rules, off-device recovery and credentials handling.
- Owner's explicit authorization for each future filesystem, terminal, public endpoint, and migration change.

## Requested sequence / deliverables

**A.** Project leadership acknowledges this WR and determines whether/when to issue a formal planning/build order to Workshop; no build authorization is implied by receipt.

**B.** Archives fulfills the separate setup WR by creating the canonical project folder and starter README/record(s) **inside the existing hub on main**, subject to its scope and rules, and returns exact paths/commit IDs.

**C.** Workshop and Security review the project foundation, propose a minimal Message Hub milestone and test/acceptance matrix.

**D.** Zed approves the implementation order before builders modify code, phone, tunnel or live services.

**E.** Substantive project plans, decisions, tests, exchanges and history live in the Archives project home; Office retains orders, short coordination and report pointers.

## Restrictions

No new repo/branch/fork; no changes to old repositories; no deployment, terminal commands, phone changes, tunnel or security changes under this WR. No secrets in GitHub. Preserve owner seals within scope, distinguish REFERENCE/HISTORICAL CLAIM/VERIFIED/ADOPTED/SUPERSEDED/UNKNOWN, and do not claim tests or build completion.

## Governing sources

- [Node 11 charter](https://github.com/Stratumnova/A25-workspace.hub/blob/main/A25-node1125_hub/README.md)
- [Workshop team rules](https://github.com/Stratumnova/A25-workspace.hub/blob/main/A25-node1125_hub/A25.office/teams/workshop/README.md)
- [Workshop Lead memory drop](https://github.com/Stratumnova/A25-workspace.hub/blob/155065c79d2494df74a19957b208e32cc350a960/A25-node1125_hub/A25.office/teams/workshop/lead/memory/A25-WORKSHOP-WK-HR-20261020T020353Z.md)
