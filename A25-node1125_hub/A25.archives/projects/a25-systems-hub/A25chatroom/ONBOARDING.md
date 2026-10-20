# A25 Chatroom — Component Onboarding

Owner: Zed
Parent project: [A25 Systems Hub](../README.md)
Status: PROVISIONAL DRAFT — awaiting owner approval of workspace layout; no build or deployment authorization

## Owner approval required

This onboarding is a provisional draft. The proposed approved structure is recorded in [Build Requests](../../build-request/a25-systems-hub-A25chatroom/README.md). Do not treat these existing files as the approved component layout until Zed explicitly accepts it.

## Work here, stay here

This folder is the permanent home of the A25 Chatroom component. Design, source, tests, fixes, evidence, recovery and handoffs remain here during active work, pauses and rebuilds. If a component breaks, investigate and repair it here without rearranging unrelated components. Package or ZIP a component for transfer or recovery while keeping its canonical repository location unchanged.

## Team exchange rooms

- [Archives inbox](archives/inbox/README.md) and [outbox](archives/outbox/README.md): custody, indexing, provenance and recovery.
- [Security inbox](security/inbox/README.md) and [outbox](security/outbox/README.md): threat, identity, permission and security reviews.
- [Builders inbox](builders/inbox/README.md) and [outbox](builders/outbox/README.md): approved build assignments and actual reports.
- [Project lead](project-lead/README.md): Workshop lead notes, dependencies, decisions and recovery.

## Team lanes and permissions

Workshop lead coordinates planning and authorized orders. Builders execute assigned scope. Security reviews security and reports evidence. Archives preserves and indexes. Zed retains owner authority. Work in your assigned area. Only leave notes in another team's inbox or folder when asked or given permission; do not edit their records. Requests are not build orders. Keep formal orders and official response records in Office, with links here to project-specific evidence.

Every new dated substantive record needs its real UTC creation time and source, author/role, status, scope, source links and record type under the Node 11 charter. Preserve original material and evidence categories: REFERENCE, HISTORICAL CLAIM, VERIFIED, ADOPTED, SUPERSEDED and UNKNOWN.

## Integration

The sibling [main build](../main%20build/README.md) is where authorized, verified component interfaces are assembled into the full system. Chatroom source and its work history stay in A25chatroom; integration should reference or package tested components, not move their development homes.

## Restrictions

Use only Stratumnova/A25-workspace.hub on main. No new repo, fork or branch; no old repository writes. No unapproved code changes, phone actions, tunnels, services or deployment. No secrets in public GitHub. Read the [Node 11 charter](../../../../README.md) and the original Workshop request before implementation.
