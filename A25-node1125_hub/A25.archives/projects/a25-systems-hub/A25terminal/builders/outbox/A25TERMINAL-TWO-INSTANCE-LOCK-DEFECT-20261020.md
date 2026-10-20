# A25terminal — Two-Instance Lock Inconsistency

**Date:** 2026-10-20
**Classification:** VERIFIED defect; production protection NOT established
**Source under test:** `src/a25_persistent_dispatcher.py` at commit `7504075a09a5468490c1903497850fd393acc0ef`, composed with `a25_persistent_lock.py` and `a25_command_supervisor.py`.

## Scope
The Android test was limited to `/storage/emulated/0/Documents/AI_Workshop/terminal tools test folder/__a25terminal_control_v1__/`. Exact root and store were verified as directories without symlink redirection. No bridge, tunnel, service, or live credential was touched.

## Reproduction
1. Create first `PersistentDispatcher` with disposable test credential-verifier callbacks and unique state file `.a25-two-instance-cdd29397a687.json`.
2. Observe first instance locked.
3. Unlock first instance with disposable owner credential; observe unlocked.
4. Construct second `PersistentDispatcher` against the SAME state file.
5. Observe both instances and the saved JSON.

## Actual observed output
```json
{"initial":{"locked":true,"active":0},"first_before_second":{"locked":false,"active":0},"first_after_second":{"locked":false,"active":0},"second":{"locked":true,"active":0},"saved":{"version":1,"locked":true},"test_file":".a25-two-instance-cdd29397a687.json"}
```

## Finding
**VERIFIED:** Two independent dispatcher objects sharing a state file can disagree on lock status. The first remains unlocked in memory after the second initializes and writes locked state. The saved state says locked. This invalidates any claim that the prototype currently enforces one global master lock.

**NOT TESTED:** A subsequent command dispatch from the first instance, actual simultaneous OS processes, outsider network access, and real bridge ingress. The discrepancy alone is a fail for the intended security design.

## Required correction
Establish exactly one trusted dispatcher owner for all callers, with exclusive ownership and authenticated ingress. Deny or safely fail closed if a second owner attempts to start. Recheck authoritative lock state atomically before command registration, and ensure lock revocation reaches all managed commands. Add tests for concurrent independent processes and restart/crash behavior before any deployment.

**Deployment decision:** HOLD. No existing terminal services changed.
