# A25 Systems Hub — Parent Project Onboarding

Owner: Zed
Status: Workspace structure established; implementation authorization pending
Governing charter: [Node 11](../../../README.md)

## One system, separate permanent component rooms

A25 Systems Hub is the overall project. Each distinct build lives in its own sibling folder under this parent and **stays there** for design, coding, testing, fixes, recovery, packaging and future continuation. Do not move a component once work starts. A component can be ZIP-packaged and restored at its same repository path. Isolate faults and fix the affected component rather than untangling a shared mixed workspace.

## Current rooms

- [A25chatroom](A25chatroom/README.md): first component; planned persistent GPT/Claude/owner messaging. Read its [component onboarding](A25chatroom/ONBOARDING.md) for Archives, Security and Builders inbox/outbox folders and Workshop project-lead notes.
- [main build](main%20build/README.md): integration area where independently verified, approved components come together to make the complete system. It is not a replacement for their original source folders.
- [Historical source index](HISTORICAL-SOURCES.md): prior repositories are read-only reference.

Future components such as terminals, tunnels, identity, storage and recovery get their own sibling folders only when their scope is actually authorized and needed. Do not invent empty project skeletons.

## Team rules and information exchange

Each component room contains its own team inbox/outbox areas as needed. Workshop lead coordinates plans and approved orders; builders perform assigned work; Security reviews security; Archives indexes and preserves; Zed controls owner decisions. Teams stay in their own lanes. Leave notes in another team's area only when asked or explicitly permitted. Cross-team requests and replies identify source, author, scope and status. Formal Office work orders and official responses remain in Office, with pointers into component records.

Use the charter's real UTC timestamps and evidence labels; never invent verification, approvals, completed tests or attribution. No forks, branches or new repositories, and no writes to historical repositories. No source implementation, live services, phone/tunnel changes or deployment without a separate approved order. No secrets in public GitHub.
