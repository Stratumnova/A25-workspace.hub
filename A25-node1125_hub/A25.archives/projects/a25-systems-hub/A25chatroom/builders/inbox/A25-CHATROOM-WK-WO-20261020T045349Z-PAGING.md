# M1 Correction — Unseen Pagination
Record: A25-CHATROOM-WK-WO-20261020T045349Z-PAGING.md
Created: 2026-10-20 04:53:49 UTC; source: container date -u
Author/role: A25-TW-GPT01, Workshop Lead
Status: ASSIGNED — NARROW STAGE 1 CORRECTION
Project: A25chatroom
Authority: owner's authorization to coordinate Chatroom build stages; no deployment authorization
Sources: [M1 retry evidence](../outbox/A25-CHATROOM-BD-RR-20261020T045156Z-M1-RETRY.md), [lead decision](../../project-lead/A25-CHATROOM-WK-ER-20261020T045349Z.md)
Baseline implementation: ef64644f11244e96000fa69085e15cc4907a8818.

Fix `ChatEngine.unseen()` so `limit` applies to messages authored by other principals after the reader's cursor, rather than filtering a limited mixed-author page. Preserve cursor semantics: read has no ack side effect, own messages never appear unseen, per-room/principal isolation, stable order, and bounded limit. Add regression test with own message(s) preceding external message(s), limit=1, and ensure correct nonempty unseen result. Run full tests with PYTHONWARNINGS=error, include exact output, commit SHA, changed paths, any new defects. Avoid unrelated refactors; no changes outside A25chatroom or to prior approval/record files.

Report to builders/outbox with evidence and stop. No new branch/repository, no phone, terminal, server, tunnel, deployment, external listener, ZIP or production auth changes. Lead will independently review before M1 acceptance.
