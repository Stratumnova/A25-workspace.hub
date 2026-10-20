# A25terminal — Persistent Lock Restart Test

**Date:** 2026-10-20
**Source revision:** `4e2c730e1051b4f65162cd51146e74bd219c3651`
**Status:** VERIFIED standalone restart/corruption behavior; integrated dispatcher persistence UNKNOWN

## Test boundary
All mutations were confined to `/storage/emulated/0/Documents/AI_Workshop/terminal tools test folder/__a25terminal_control_v1__/`. The authorized root and store were verified to exist, be directories, and not be symlinks. The exact GitHub source was downloaded to `a25_persistent_lock_test.py` and tested against `.a25-persistent-lock-test.json` in the same folder. No services were restarted or altered.

## Observed result
```json
{"starts_locked":true,"unauthorized_unlock_rejected":true,"owner_unlock":true,"restart_locked":true,"corrupt_state_locked":true,"final_state":{"version":1,"locked":true}}
```

## Interpretation
**VERIFIED:** Fresh instance locks by default; unverified unlock rejected; verified-owner flag unlocks; fresh instance relocks; corrupt JSON state relocks and rewrites a valid locked record. Final test state locked.

**UNKNOWN:** Cross-process exclusivity, filesystem race resistance, safe state ownership, process crash during atomic replace, durability under sudden power loss, real owner credential verification, and integration with supervisor and caller authentication. The test uses a boolean `owner_verified` supplied by trusted code; it is not itself authentication.

**KNOWN LIMITATION:** This component is standalone. Two independent instances do not share an in-memory guard; production callers must be routed through one trusted owner process. The code does not secure legacy bridges or direct shell access.

## Next
Integrate fail-closed state into the single-owner dispatcher and test concurrent requests in one process. Separately design authenticated ingress and exclusive ownership before deployment.
