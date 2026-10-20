# A25terminal — Exclusive Owner Android Retest

**Date:** 2026-10-20
**Source:** `src/a25_exclusive_owner.py` commit `ddc0ea1003e92fff1ad2bc288a8f28989182892d`
**Status:** VERIFIED failure to acquire advisory lock; root cause UNKNOWN; deployment HOLD

## Scope and preserved artifacts
Authorized root `/storage/emulated/0/Documents/AI_Workshop/terminal tools test folder`, store `__a25terminal_control_v1__`. Root and store were verified directories, not symlinks. Read-only inspection found prior `a25_exclusive_owner_test.py` (1807 bytes) and `.a25-owner-isolation-test.lock` (0 bytes), both present and not symlinks. No deletion or overwrite.

## Retest
Used the existing source test copy and a fresh unique disposable lock filename inside the authorized store. Attempted first `ExclusiveOwner(lock)`; planned child process contention test only after successful acquisition; cleanup guarded against undefined first-owner variable.

Actual observed JSON:
```json
{"error":"RuntimeError: STOP: dispatcher owner already active or lock unavailable","reacquire_error":"RuntimeError: STOP: dispatcher owner already active or lock unavailable"}
```

## Findings
**VERIFIED:** The first lock acquisition failed; after cleanup, acquisition failed again. No second process contention test could be performed. The original test's `NameError` was a test-harness cleanup issue, not evidence that exclusive locking worked.

**UNKNOWN:** Exact OS error/errno, whether Android emulated shared storage rejects `flock`, and whether an alternate filesystem or owner-process design is appropriate. Do not interpret this as proof another owner is active.

**KNOWN:** Advisory locks would protect only cooperating processes even if functional. This component is not connected to ingress, and does not secure existing bridges.

## Decision
**HOLD deployment.** Diagnose filesystem lock support read-only or in isolated test scope; choose an exclusive single-owner architecture with verified OS semantics. Do not modify legacy services or move tests outside the owner's exact authorized folder without further approval.
