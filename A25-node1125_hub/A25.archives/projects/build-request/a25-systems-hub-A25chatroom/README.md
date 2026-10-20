# A25 Chatroom Workspace — Approval Request

Owner/approver: Zed
Requested by: Archives workspace preparation following Workshop setup request
Status: DRAFT — AWAITING OWNER APPROVAL
Proposed approved destination: `A25.archives/projects/a25-systems-hub/A25chatroom/`
Parent: [A25 Systems Hub](../../a25-systems-hub/README.md)

## Proposed component layout

```text
a25-systems-hub/
  A25chatroom/
    README.md
    ONBOARDING.md
    archives/
      inbox/
      outbox/
    security/
      inbox/
      outbox/
    builders/
      inbox/
      outbox/
    project-lead/
      README.md
  main build/
    README.md
```

This is the first component of a wider modular A25 Systems Hub. Future terminals, tunnels and other components receive separate sibling folders only when needed. Each component stays at its own canonical location throughout design, build, tests, repair, recovery and ZIP packaging. Main build assembles authorized, verified components without relocating their source or work history.

## Proposed team workflow

Archives indexes and preserves; Security reviews security; builders perform assigned work; Workshop/project lead coordinates notes, dependencies and orders; Zed approves. Each team uses its own inbox/outbox, and places notes in another team's area only when asked or permitted. Formal Office orders and official responses remain in Office, linked from the component.

## Current correction

The folders and onboarding files were created under A25chatroom before the owner-approval staging rule was established. They are **provisional working drafts, not owner-approved layout**. This request records the intended approved structure. Do not treat the existing folders as accepted simply because they are already present.

## Approval gate

Await Zed's explicit acceptance or requested changes. After approval, synchronize the approved text to A25chatroom and record the approval source. No component implementation, live service, terminal/tunnel changes or deployment is authorized by layout approval alone.

Sources: [Workshop build authorization request](https://github.com/Stratumnova/A25-workspace.hub/blob/main/A25-node1125_hub/A25.office/teams/workshop/requests/incoming/A25-SYSTEMS-HUB-WK-WR-20261020T020916Z.md); [Node 11 charter](../../../README.md).
