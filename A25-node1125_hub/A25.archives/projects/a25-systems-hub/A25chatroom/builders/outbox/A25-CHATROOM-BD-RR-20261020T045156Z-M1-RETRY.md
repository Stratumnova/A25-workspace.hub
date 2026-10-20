# A25 Chatroom M1 Verification Retry — Evidence Report

Record ID: A25-CHATROOM-BD-RR-20261020T045156Z-M1-RETRY.md
Time: 2026-10-20 04:51:56 UTC, isolated container `date -u`
Author/role: GPT, A25 Chatroom builder verifier
Type: RR
Status: **VERIFIED SIX TESTS PASS; KNOWN PAGINATION DEFECT REPRODUCED; M1 ACCEPTANCE RESERVED TO LEAD**
Order: [M1 retry order](../inbox/A25-CHATROOM-WK-WO-20261020T045040Z-M1-RETRY.md)
Exact target commit: `ef64644f11244e96000fa69085e15cc4907a8818`
Repository: Stratumnova/A25-workspace.hub, existing main branch.

## Source integrity — VERIFIED

Retrieved exact file content from GitHub connector `fetch_file` with explicit ref `ef64644f11244e96000fa69085e15cc4907a8818`; transferred source bytes to isolated directory `/mnt/data/m1_retry_exact`. For each file independently calculated `SHA1(b"blob " + str(len(bytes)).encode() + b"\\0" + bytes)` and compared with GitHub-returned blob SHA. The transferred files were not modified after hashing.

| Relative path | Bytes | Computed and GitHub blob SHA | Result |
|---|---:|---|---|
| `chat_engine/__init__.py` | 49 | `730d3795e2c73a6d9b12f5ac4be00463b1ee027e` | MATCH |
| `chat_engine/engine.py` | 5233 | `363ff531c68ecda20471e736ebf7d23a12d4d9b1` | MATCH |
| `tests/test_engine.py` | 3412 | `1b6ee95049769d0d82f67d19630b0b8e1d543dc4` | MATCH |

Git network checkout attempt still failed with `Could not resolve host: github.com`; authorized connector source transfer plus independent blob-hash verification was used instead. Documentation file was connector-read at same commit (GitHub blob `03c5a4ab1ea2e63672b12cb32720ba070654bd40`), but was not locally transferred or hash-verified. Runtime imports resolved from the verified local source tree.

## Exact six-test run — VERIFIED

Environment: Python `3.13.5`, SQLite `3.46.1`; isolated local filesystem, no server or external services.

Command from `/mnt/data/m1_retry_exact`:
```sh
PYTHONWARNINGS=error python -m unittest discover -s tests -v
```

Full combined stdout/stderr:
```text
test_concurrency (test_engine.Tests.test_concurrency) ... ok
test_cursors (test_engine.Tests.test_cursors) ... ok
test_idempotent_retry (test_engine.Tests.test_idempotent_retry) ... ok
test_invalid_and_spoof (test_engine.Tests.test_invalid_and_spoof) ... ok
test_restart_and_rollback (test_engine.Tests.test_restart_and_rollback) ... ok
test_rooms_and_authors (test_engine.Tests.test_rooms_and_authors) ... ok

----------------------------------------------------------------------
Ran 6 tests in 0.238s

OK
EXIT:0
```

All six committed tests passed; exit 0; no warnings or resource leaks observed in this run. This is not proof that no leak can occur under other workloads.

## Independent probes — VERIFIED

Ran a separate inline Python probe importing the same byte-verified `chat_engine` module, using a new temporary SQLite DB:

- **Cross-process reopen/persistence:** wrote a message and cursor, launched `subprocess.run([sys.executable, "-c", ...])` to create a fresh ChatEngine instance in a distinct Python process. Output: `RESTART 0 'survives 1\\n' ''` (exit 0, message and cursor preserved).
- **Concurrent writes:** 12 worker threads posted 100 uniquely keyed messages. Output `CONCURRENT 100 100 100` (100 returned, 100 distinct sequences, 100 rows in default first read page after initial persisted message; note: default page limit is 100, so this last figure does not count all 101 rows).
- **Rollback:** raised `RuntimeError` inside `with e.db()` after an INSERT, then checked the record was absent. Output `ROLLBACK True`.
- **Pagination defect:** posted own message then another participant's message in a fresh room, called `unseen(room, actor, limit=1)`. Output `PAGING [] EXPECTED_EXTERNAL_COUNT 1`. **Defect confirmed**: own-message filtering after the LIMIT hides later external unread messages.
- **Warnings:** committed tests run with `PYTHONWARNINGS=error` passed without resource warnings. Independent probe did not elevate warnings to errors; no warnings observed.

Exact remaining probe output:
```text
RESTART 0 'survives 1\n' ''
CONCURRENT 100 100 100
ROLLBACK True
PAGING [] EXPECTED_EXTERNAL_COUNT 1
SQLITE 3.46.1 PYTHON 3.13.5
20261020T045156Z
```

## Provenance, limitations, and decisions

**VERIFIED:** The three executable files match GitHub blob IDs from the specified target commit; six committed tests pass locally; cross-process persistence, concurrent unique sequencing and rollback pass independent probes; the pagination defect is reproducible.

**UNKNOWN:** Full repository checkout/diff audit (DNS unavailable); broader multi-process stress, crash/power-loss durability, production authentication, authorization and connector integration. No runtime deployment performed.

**HISTORICAL CLAIM / unresolved chronology:** Prior builder report bears `04:44:35`, earlier than provisional `04:46:00` Stage 1 order. The Stage 1 order explicitly labels its timestamp provisional. No verified commit chronology was established for these original records in this retry; preserve both, do not silently resolve.

**Recommendation:** Workshop Lead can review six-test evidence for M1 gate. Correct and regression-test `unseen()` pagination before downstream reliance, under a **separate authorized change order**. Security must review trusted Actor injection seam before any untrusted interface. This report does not assert M1 acceptance.

No source changes, branches, deployment, phone, server, tunnel or listener operations. Sole GitHub write: this new outbox report.
