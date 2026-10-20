# A25 Systems Hub — Canonical Project Home

Owner: Zed
Responsible implementation team: A25 Workshop
Archives custody: A25 Archives
Status: Project landing established; Workshop planning/build authorization requested, not granted by this document
Repository: Stratumnova/A25-workspace.hub
Branch: main
Charter: [Node 11 root charter](../../../README.md)

## Purpose and project boundary

The A25 Systems Hub is the planned official successor to the historical Pocket Server / Workstation Roundtable 01. The initial functional milestone is a persistent **Message Hub** for Zed, GPT and Claude. This folder is the single active and permanent project home; do not create a separate active-session tree or migrate the project when work pauses.

**Owner cutoff:** 2026-10-19 20:07 MDT / 2026-10-20 02:07 UTC. All prior Pocket Server work is historical reference, not automatically adopted architecture, code or implementation for the successor. Preserve original records and valid owner seals within their scope. Later reports likewise require evidence and explicit adoption.

## Planned workstreams — proposed, not implemented

1. Persistent, restart-recoverable Message Hub with durable message identity, timestamps, authorship, ordered delivery and audit trail.
2. GPT-led, Claude-led and Shared Roundtable areas. All three participants may read and contribute to each; the area names designate leadership, not private access.
3. Local-first working files and protected runtime storage, with GitHub as version-history/backup mirror rather than live message database.
4. Independent authenticated owner, GPT and Claude identities with server-enforced permissions.
5. Independent secure server, bridges and tunnels rather than unreviewed reuse of the historical bridge.
6. Controlled terminal/workshop access, action audit and separation of messaging from command execution.
7. Backups, restore checks, recovery, independent verification, owner-approved migration and eventual retirement of the old Pocket Server.

## Component workspaces and onboarding

Read [parent onboarding](ONBOARDING.md). The first self-contained build is [A25chatroom](A25chatroom/README.md), with its own [component onboarding](A25chatroom/ONBOARDING.md), Archives, Security and Builders inbox/outbox rooms, and Workshop [project-lead notes](A25chatroom/project-lead/README.md). The sibling [main build](main%20build/README.md) is the integration area for approved, independently verified components.

Every future component (terminals, tunnels and others) receives its own permanent sibling folder when needed. Design, code, tests, repairs and recovery stay with the component, even when ZIP-packaged or integrated into the main build. Formal Office authority remains separate.

## Source and coordination links

- [Archives setup request](../../../A25.office/teams/archives/requests/incoming/A25-SYSTEMS-HUB-AG-WR-20261020T020916Z.md)
- [Workshop planning/build-order authorization request](../../../A25.office/teams/workshop/requests/incoming/A25-SYSTEMS-HUB-WK-WR-20261020T020916Z.md)
- [Historical source index](HISTORICAL-SOURCES.md)
- [Workshop team](../../../A25.office/teams/workshop/README.md)
- [Archives team](../../../A25.office/teams/archives/README.md)

## Local-first placement recommendation — not executed

The owner-planned shared document root is `Documents/A25-node1125_hub/` on Android. Its project tree should mirror this canonical project location. Shared Documents should contain only files suitable for that visibility. Keep runtime databases, tokens, credentials, private keys, protected configuration and other sensitive operational state in access-controlled Termux-private storage, outside public GitHub and ordinary shared Documents. The actual checkout, storage mounts, ignore rules, encryption, backup and sync strategy require Workshop/Security design and owner approval. No phone files or services have been changed.

## Current status and recovery

**VERIFIED:** Original Workshop and Archives work requests were fetched from the official repository; this landing was created as an Archives documentation action.

**REFERENCE:** Historical Pocket Server, Gate-01/02, Shared Space, bridge/tunnel and related reports; see the source index.

**UNKNOWN / NOT YET AUTHORIZED:** Implementation design, authenticated runtime, tested Message Hub, migration, live server changes, builder assignments and cutover.

To resume: read this README, the two original requests and the historical-source index; consult the latest actual Office order and evidence before acting. Do not treat project setup as implementation approval. Add substantive plans, tests, findings and recovery records here only when real work produces them.

## Restrictions

No fork, new branch or repository. No writes to old repositories. No source implementation, phone/terminal actions, tunnels, deployments, migrations or old-system retirement under this setup request. Preserve original evidence and distinguish REFERENCE, HISTORICAL CLAIM, VERIFIED, ADOPTED, SUPERSEDED and UNKNOWN. No secrets or private materials in public GitHub.

## Build request and approval path

New component proposals begin in [build-requests](build-requests/README.md), separate from the component workspaces. The [Message Hub proposal](build-requests/A25-MESSAGE-HUB-WORKSHOP-PROPOSAL-001.md) is pending owner review. Only after Zed explicitly approves a version should that approved version be placed in [A25chatroom](A25chatroom/README.md), with the original proposal retained as an identifiable historical record. Each later component follows the same pattern. Approval of a plan does not automatically authorize implementation.
