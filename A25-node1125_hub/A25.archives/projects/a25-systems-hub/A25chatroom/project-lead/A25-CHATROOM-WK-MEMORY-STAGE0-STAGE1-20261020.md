# A25 Chatroom — Durable Workshop Memory: Stages 0–1

**Owner:** Zed. **Accountable lead:** A25-TW-GPT01. **Status:** CP0 accepted; M1 accepted for isolated sandbox functionality; Stage 2 Security review pending.

## Leadership accountability — owner-directed
The GPT builder operates under the same GPT account and leadership chain as the Workshop Lead. The Lead writes the order, the GPT builder performs the work and reports, and the Lead reads and accepts or rejects the report. **Once the Lead accepts the work, the Lead owns its results as team work, as if the Lead had performed it personally.** Do not discount a builder's verified labor or distance the Lead from its quality. The Lead may ask for more evidence before acceptance; after acceptance, accountability stays with the Lead. Zed's choice not to stop accepted progress is his approval of continuing with that work, with the same leadership accountability. This is an owner-adopted governance rule, not a claim that Zed personally operated the terminal. A Claude builder would be a separate conversation/account and must be attributed distinctly.

For technical reproducibility, retain who physically executed a command and where, without using that distinction to evade ownership. An accepted GPT builder PASS is the Workshop Lead's PASS and responsibility; sandbox evidence remains sandbox evidence rather than physical-terminal proof.

## Project scope
[Owner-approved V1](../APPROVED-BUILD-PLAN-V1.md): persistent text-only named rooms for Zed, GPT and Claude, user-invoked existing interfaces, no paid model API and no autonomous model-to-model loop. Only Zed may clear a live room after verified archival. Plan approval does not alone prove implementation. Existing `main` and A25chatroom project only; no phone/server/tunnel/deployment without separate authorization.

## Stage 0 — CP0
[Builder reconnaissance](../builders/outbox/A25-CHATROOM-BD-RR-20261020T044135Z.md), report commit `75b8fef3edc7341a760c9e00ced9df36d0812c97`; [stage plan](A25-CHATROOM-WK-WO-20261020T043822Z.md). Proposed Python/SQLite persistent engine, append-only ordered messages, explicit cursors, and trusted Actor seam. **CP0 accepted as design; no executable tests were run.**

## Stage 1 — Build, tests, defect and correction
1. **Initial implementation:** commit `ef64644f11244e96000fa69085e15cc4907a8818`; [builder report](../builders/outbox/A25-CHATROOM-BD-RR-20261020T044435Z.md), report commit `b16977ced971f1b84978acb96c4295ab557743b0`. Local-only `chat_engine/__init__.py`, `chat_engine/engine.py`, `tests/test_engine.py`, `docs/CHAT-ENGINE-INTERFACES.md`.
2. **Initial test access blocked:** [block report](../builders/outbox/A25-CHATROOM-BD-RR-20261020T044833Z-M1-VERIFY.md), commit `e8cb0077993a867c79d51f7fe25900d20d65fe35`. Git checkout failed DNS. No PASS from blocked attempt.
3. **Owner-approved retry and six tests:** [retry order](../builders/inbox/A25-CHATROOM-WK-WO-20261020T045040Z-M1-RETRY.md), commit `ae5ca6abb18cd7985db2c4bd296d4082f6c5f656`; [full six-test report](../builders/outbox/A25-CHATROOM-BD-RR-20261020T045156Z-M1-RETRY.md), commit `6116cd5c65f10a70cd13d7ececaf78267f7c1d6b`. Three files byte-verified against GitHub blobs; Python 3.13.5 / SQLite 3.46.1. `PYTHONWARNINGS=error python -m unittest discover -s tests -v`: **6 PASS, 0 failures, exit 0, no warnings**. Independent probes: cross-process persistence PASS, 100 unique concurrent writes PASS, rollback PASS. Pagination probe exposed defect: `unseen(limit=1)` could return empty if own messages preceded external unread messages.
4. **Narrow fix:** [pagination correction order](../builders/inbox/A25-CHATROOM-WK-WO-20261020T045349Z-PAGING.md), commit `a1bdf00e38c865c21b05751a9bc3e2b08d74f5f5`. SQL filters external authors before LIMIT; regression test added. Corrected implementation commit `1de61b9926819c6b8173a4d839cb248b1b1715bb`.
5. **Conflicting interim reports preserved:** builder conversational claim of seven-test PASS and blocked GitHub report write versus [committed report](../builders/outbox/A25-CHATROOM-BD-RR-20261020T045800Z-PAGING.md), commit `1fb8d3958a0f8c61383506ac47d42b62418dfad8`, reporting inability to execute corrected source. Neither was the final acceptance basis.
6. **Final verification:** [order](../builders/inbox/A25-CHATROOM-WK-WO-20261020T050636Z-M1-FINAL.md), commit `e6e64343061d78bc42f95e3244d09215f18cafd6`; [full seven-test receipt](../builders/outbox/A25-CHATROOM-BD-RR-20261020T050733Z-M1-FINAL.md), report commit `fc302758bcae11e30fe79e8be1c6b163c1186df8`. All three GitHub blob hashes matched local test files. Python 3.13.5 / SQLite 3.46.1; exact warnings-as-errors command; **7 PASS, 0 failures, exit 0, no warnings**.
7. **Lead acceptance:** [M1 decision](A25-CHATROOM-WK-ER-20261020T051100Z.md), commit `38b2f656f3d24ce3c7fd356655d2baeffd68f570`. The Workshop Lead **owns and accepts the seven-test result as its team's work**. M1 accepted for isolated local functionality, not production/physical operation.

## Test inventory — why and outcome
| Test | Purpose | Accepted result |
|---|---|---|
| `test_rooms_and_authors` | Room separation and actor attribution | PASS |
| `test_idempotent_retry` | Prevent duplicate posts | PASS |
| `test_cursors` | Explicit monotonic ack, unseen classification, room isolation | PASS |
| `test_restart_and_rollback` | SQLite persistence and rollback | PASS |
| `test_concurrency` | Concurrent write integrity and unique sequence numbers | PASS |
| `test_invalid_and_spoof` | Reject invalid input and payload-based spoofing in local actor seam | PASS; not production authentication |
| `test_unseen_pagination_skips_own_messages` | Regression for own messages hiding external unread messages | PASS |
| Extra separate-process, 100-write, rollback probes | Extend initial behavior checks | PASS |
| Pre-fix pagination probe | Reproduce suspected bug | DEFECT CONFIRMED, corrected and regression-tested |

Full output, environment, hashes and commands: [six-test report](../builders/outbox/A25-CHATROOM-BD-RR-20261020T045156Z-M1-RETRY.md) and [seven-test report](../builders/outbox/A25-CHATROOM-BD-RR-20261020T050733Z-M1-FINAL.md). The GPT builder ran actual Python tests in an isolated cloud sandbox, not GitHub Actions and not a physical target terminal. **Lead accountability for accepted results is not reduced by delegated execution.**

## Pending / next
[Security identity-seam request](../security/inbox/A25-CHATROOM-WK-IR-20261020T044600Z-SEC.md) remains open. Stage 2 must independently enforce Zed/GPT/Claude identities, prevent AI clearing/deleting, and require verified archival for owner-only clear. Production security, target-terminal operation, crash durability, and real connector integration are UNKNOWN. Security review is not implied by M1 acceptance.

## Owner blocked-operation rule
[Standing record](A25-CHATROOM-WK-OD-20261020T050027Z.md): blocked terminal or GitHub operation means STOP, inform Zed of exact operation/target/error, request approval for identical retry. No silent alternative method or changed scope.

## Stage recap protocol
At each stage, create a new dated `project-lead/` recap covering authority, builder order, work performed, implementation and report SHAs, tests and reasons, full evidence links, defects, blocked attempts/owner approvals, lead acceptance and ownership, Security/Archives input, unresolved items, and next action. Preserve original evidence and disagreements. Owner non-intervention permits continuation of accepted work but is not falsely recorded as direct terminal execution.
