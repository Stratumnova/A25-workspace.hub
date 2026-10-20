# A25terminal — Persistent Dispatcher Integration Test

**Date:** 2026-10-20
**Source revision:** `7504075a09a5468490c1903497850fd393acc0ef`
**Status:** VERIFIED isolated in-process integration; cross-process and ingress security UNKNOWN

## Boundary and method
Verified exact Android root `/storage/emulated/0/Documents/AI_Workshop/terminal tools test folder` and contained `__a25terminal_control_v1__` directory. Loaded source for `a25_persistent_lock.py`, `a25_command_supervisor.py`, and `a25_persistent_dispatcher.py` into the authorized test folder. Used isolated `.a25-integrated-lock-test.json` state and disposable trusted credential-verifier callbacks, not real owner credentials. Existing terminal bridge/tunnel/service unchanged.

## Observed output
```json
{"initial":{"locked":true,"active":0},"initial_reject":true,"authorized_exit":0,"outsider_reject":true,"active_before":1,"lock":{"locked":true,"failed_to_stop":[],"new_dispatch_blocked":true},"worker_finished":true,"after_lock":{"locked":true,"active":0},"unlocked_before_restart":true,"restart_locked":true}
```

## Evidence
**VERIFIED:** Initial lock rejects commands; trusted owner verification unlocks; authorized read-only disposable command exits 0; simulated outsider rejected while unlocked; managed 30-second disposable process tracked and terminated on lock; no active managed commands remain; new dispatcher instance starts locked even after prior instance unlocked.

**UNKNOWN:** Exclusive cross-process ownership, concurrent independent client ingress, credential transport security, filesystem races, full process-tree termination, Android shared-storage permission guarantees, audit durability, real external outsider reachability, and integration with legacy terminal routes. The new dispatcher is a local test class, not an installed service.

**Design caution:** Each independent instance has its own supervisor and can be unlocked independently. Persistence defaults a *new* instance to locked, but does not make simultaneous instances a single security boundary. A trusted single-owner ingress process is required before deployment.

## Next
Test simultaneous threads against one instance and explicit failure paths. Design a single-owner authenticated ingress without modifying existing bridges. Record any failure instead of claiming production readiness.
