# A25 Systems Hub — Workshop Build Plan Proposal 001

**Author:** A25-TW-GPT01, Workshop Lead
**Owner:** Zed
**Status:** PROPOSED FOR OWNER AND ARCHIVES REVIEW — NOT ADOPTED OR AUTHORIZED TO BUILD
**Repository:** Stratumnova/A25-workspace.hub, existing main
**Project home:** A25-node1125_hub/A25.archives/projects/a25-systems-hub/
**Record:** Workshop proposal 001; this document is not an Office work order or implementation receipt.
**Historical boundary:** 2026-10-19 20:07 MDT / 2026-10-20 02:07 UTC

## Goal

Build a **free-of-paid-model-API, persistent, text-only, multi-conversation team Message Hub** for Zed, GPT and Claude. It is the first functional milestone of A25 Systems Hub, which will eventually replace the current Pocket Server. Zed continues using the existing ChatGPT and Claude interfaces; the assistants use authorized terminal/connector access to read and post in a shared chat area when prompted. This is not a new model-powered chat application, and there is no autonomous model-to-model loop.

The project README identifies additional later workstreams: local-first files, authenticated identities, independent server/bridges/tunnels, controlled workshop terminal tools, backups and verified migration. This proposal focuses on **Message Hub V1**; later systems require separate planning and orders.

## Owner-directed behavior

- Zed, GPT and Claude can create named conversations/rooms, read, post and participate in group discussion.
- Multiple independent conversations may be opened and continued. Text messages only; **no file attachments in the chat**. Files, builder outputs and future file-return bots belong to other A25 systems.
- Assistants act when prompted through their existing interfaces, for a short task, then return. No paid AI API calls or background auto-conversation.
- The instruction controls behavior. Examples: **check chat** (read and briefly report), **scan conversation** (read context and discuss back in original interface), **respond there** (post to the specified room and briefly report back), **continue discussion** (participate in room as instructed). Do not assume reading authorizes a reply.
- When posting, the assistant identifies its author accurately, can include the owner-requested conversational sign-off such as `zed-check chat @9:16pm oct19`, and reports briefly back in the invoking interface. Actual attribution comes from authenticated identity, not the text signature.
- Corrections are ordinary follow-up messages. Do not create a special revision workflow.
- GPT and Claude may **never delete or clear** messages, rooms or archives. Only Zed can clear a live room, after archival. Normal operations destroy nothing.
- A cleared live room's preserved archive remains available for reimport. Clearing a view and permanent destruction are not equivalent.

## Portable chat ZIPs — Workshop functionality, Archives custody

- Export **all conversations, selected conversations, one whole conversation, or selected individual messages**. Support filtering by author (Zed, GPT, Claude), including complete per-author exports.
- Exports preserve room IDs, message IDs, authors, timestamps, order, and relevant metadata. Provide human-readable text (Markdown) and structured data (JSON) in a ZIP with manifest and integrity hashes; this is a **proposed implementation format**, subject to review.
- Export must not alter the source chat or read cursors.
- Import a valid A25 chat ZIP, display its history as a normal readable conversation, and **continue appending new messages**. Preserve original imported messages unchanged. Re-export may include imported history plus new messages.
- Reimporting the same data must not silently duplicate messages. Mark provenance of imported data and validate ZIP content safely before loading.
- Original ZIP files remain intact; Archives, **not Workshop**, decides archive locations, naming, custody, retention and organization. Workshop supplies export/import mechanics and interfaces.
- No chat attachments: **ZIP import/export is a conversation portability operation outside ordinary message posting**, not a general-purpose attachment feature.

## Proposed implementation stages (not work orders)

**Stage 0 — Confirm scope and interfaces.** Archives/owner review this proposal; Security reviews identity, storage and access. Document what existing connector/terminal capabilities can actually support without paid AI APIs. No assumption that a GPT/Claude client can silently synchronize outside user-initiated tool calls.

**Stage 1 — Core text chat.** Local persistent storage with room creation/listing, append-only messages, author identity, timestamps, ordering, room history and per-participant read position. Server survives restart. Minimal terminal-friendly commands/tools to list, read, post and select rooms. Distinguish read from reply.

**Stage 2 — Auth and permission enforcement.** Separate owner/GPT/Claude principals at the service boundary; role-based operations. Deny deletion/clear to both AIs. Zed-only clear after archive verification. No reliance on message text to prove identity. Keep secrets out of shared Documents/public GitHub. Security review before network exposure.

**Stage 3 — ZIP portability.** Deterministic exports for whole/selected rooms, selected messages and author-filtered sets; manifests/checksums; safe import with original IDs/provenance; continuation without rewriting originals; round-trip and duplicate-import tests. Provide a way to inspect an imported ZIP before activating it.

**Stage 4 — Existing-interface integration.** Connect user-invoked GPT and Claude terminal/connector workflows to read/post operations. Report success only after actual server acknowledgment. Confirm short task-and-return behavior, no paid model API calls.

**Stage 5 — Reliability and acceptance.** Restart recovery, two-client concurrency, ordering, cross-identity isolation, authorization denials, import/export recovery, archive-before-clear gate, malformed ZIP rejection, and backup/restore verification. Run separately from the existing Pocket Server until owner authorizes cutover.

## Acceptance scenarios for owner review

1. Zed creates two rooms. GPT and Claude can each enter either room, see the correct history and add text without paid AI API calls.
2. Zed tells GPT `check chat`: GPT reads and returns a short report **without posting**. Zed then explicitly asks for a response: GPT posts in the correct room, with verifiable attribution, and returns a short receipt.
3. A fresh session can read previous history and distinguish unread messages from already-seen context.
4. Export all rooms, one room, a group of rooms, selected messages and GPT-only/Claude-only/Zed-only messages; original live messages are unchanged.
5. Import an exported room ZIP, display it, continue chatting, export the expanded room again; the first ZIP and its messages remain unchanged.
6. Duplicate import does not duplicate message records. Corrupt/malicious ZIPs are rejected without altering live history.
7. GPT/Claude attempts to clear or delete are denied by the server. Zed can clear a room only after a readable archive is verified; no original archive is destroyed.
8. Restart and restore preserve authors, room identity, order and history. No changes to the historical Pocket Server are required for the test.

## Dependencies and unresolved technical choices (not extra feature requests)

- Verify available GPT/Claude connectors and whether both can invoke the needed operations within their existing subscriptions and session limits.
- Choose minimal persistent storage, message schema and export ZIP schema; Security to assess threats and protections.
- Agree on how Zed accesses the text room from the terminal, while GPT/Claude operate via connectors.
- Determine separate test runtime and safe network exposure. No deployment or cutover under this proposal.
- Archives to review project record placement and archive handoff; owner to approve scope and implementation order.

## Boundaries and evidence

All builds before the owner cutoff are **REFERENCE**, not automatically accepted successor code or design. Prior claims and tests require fresh verification; an owner-adopted design does not prove implementation. Preserve originals and classify REFERENCE / HISTORICAL CLAIM / VERIFIED / ADOPTED / SUPERSEDED / UNKNOWN.

This plan **does not** authorize builders, create an Office order, change Android/Termux, run services, alter existing tunnels, migrate code, or retire the Pocket Server. Zed and Archives review first.

## Source pointers

- [Canonical project README](../README.md)
- [Historical source index](../HISTORICAL-SOURCES.md)
- [Original Workshop work request](../../../A25.office/teams/workshop/requests/incoming/A25-SYSTEMS-HUB-WK-WR-20261020T020916Z.md)
- [Archives setup response](../../../A25.office/teams/archives/requests/responses/A25-SYSTEMS-HUB-AG-RR-20261020T022505Z.md)
