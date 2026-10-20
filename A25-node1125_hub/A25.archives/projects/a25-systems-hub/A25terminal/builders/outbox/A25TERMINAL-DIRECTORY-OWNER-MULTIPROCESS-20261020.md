# A25terminal — Independent-Process Directory Owner Test

**Date:** 2026-10-20
**Status:** VERIFIED two-process result; NOT a completed security boundary
**Deployment:** HOLD

## Scope
Only authorized Android test folder `/storage/emulated/0/Documents/AI_Workshop/terminal tools test folder/__a25terminal_control_v1__/`. Verified root and store directories and absence of symlink redirection. A fresh unique directory marker was created; it remains preserved. No live bridge or service was modified.

## Test
Parent spawned two independent Python child processes, each attempting `os.mkdir(marker, 0o700)` after a short equal delay. Both were awaited with timeout; stdout, stderr and exit status were captured.

Actual observed result:
```json
{"a":{"exit":0,"stdout":"{\"result\": \"denied_exists\"}","stderr":""},"b":{"exit":0,"stdout":"{\"result\": \"acquired\"}","stderr":""},"marker_exists":true,"marker_name":".a25-multiprocess-owner-f0d932a7c037"}
```

## Evidence classification
**VERIFIED:** Exactly one of two competing independent processes created the marker, and the other observed `FileExistsError`. Both exited normally. Marker remained.

**UNKNOWN:** Higher concurrency, process-crash/restart semantics, external deletion of markers, secure authentication and ingress, and integration with managed command cancellation.

**Limitation:** Directory creation alone cannot identify a live owner and is not an authenticated IPC channel. The prototype's `release()` does not remove the marker, intentionally causing fail-closed restart denial pending manual review. Do not deploy as complete security control.

## Next justified work
Prototype authenticated single-owner command ingress without changing existing services; specify crash-recovery review and non-bypassable routing before any production installation.
