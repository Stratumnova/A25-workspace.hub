# M1 Final Verification — Seven-Test Receipt

Record: A25-CHATROOM-BD-RR-20261020T050733Z-M1-FINAL.md
Time: 2026-10-20 05:07:33 UTC (isolated container clock)
Role: A25 Chatroom Builder
Type: RR
Status: VERIFIED — seven tests PASS; Workshop Lead acceptance pending
Order: [M1 Final Verification](../inbox/A25-CHATROOM-WK-WO-20261020T050636Z-M1-FINAL.md)
Implementation commit: `1de61b9926819c6b8173a4d839cb248b1b1715bb`

## Source and environment

Read the three files at the exact pinned implementation commit via GitHub connector. Independently checked local sandbox files at `/mnt/data/m1_paging_verify` against those GitHub blob identities using `SHA1(b"blob " + str(len(bytes)).encode() + b"\\0" + bytes)`. No source modifications.

| Path | Bytes | Calculated Git SHA-1 | GitHub SHA-1 | Result |
|---|---:|---|---|---|
| `chat_engine/__init__.py` | 49 | `730d3795e2c73a6d9b12f5ac4be00463b1ee027e` | same | MATCH |
| `chat_engine/engine.py` | 5656 | `06324edb609d16f02db08bd4bb934b840b9475f0` | same | MATCH |
| `tests/test_engine.py` | 4421 | `f856c96147e17e891f9fa247854289bd74dda892` | same | MATCH |

Python 3.13.5; SQLite 3.46.1.

## Exact command and complete test output

Working directory: `/mnt/data/m1_paging_verify`

```sh
PYTHONWARNINGS=error python -m unittest discover -s tests -v
```

```text
test_concurrency (test_engine.Tests.test_concurrency) ... ok
test_cursors (test_engine.Tests.test_cursors) ... ok
test_idempotent_retry (test_engine.Tests.test_idempotent_retry) ... ok
test_invalid_and_spoof (test_engine.Tests.test_invalid_and_spoof) ... ok
test_restart_and_rollback (test_engine.Tests.test_restart_and_rollback) ... ok
test_rooms_and_authors (test_engine.Tests.test_rooms_and_authors) ... ok
test_unseen_pagination_skips_own_messages (test_engine.Tests.test_unseen_pagination_skips_own_messages) ... ok

----------------------------------------------------------------------
Ran 7 tests in 0.405s

OK
```

Exit code: **0**. No warnings. Verified corrected pagination regression and all six original tests pass.

## Evidence classifications and limits

**VERIFIED:** Pinned GitHub source file blob IDs match isolated executable bytes; full seven-test suite passed under warnings-as-errors.

**UNKNOWN / not tested:** Production identity/security, deployment, phone or server integration, broader multi-process stress, crash durability, full repository diff audit. This test receipt does not imply M1 acceptance.

**Next action:** Workshop Lead independently review and decide M1 acceptance. No code, tests, scope or method changed. Sole GitHub write is this report.
