# A25terminal — Single Dispatcher Integration Test

**Date:** 2026-10-20
**Source revision:** `77cc29b7af07309f99710ea71be1a66f96e343ff`
**Status:** VERIFIED isolated single-process integration; service, persistence, and alternate ingress UNKNOWN

## Authorized test scope
`/storage/emulated/0/Documents/AI_Workshop/terminal tools test folder/__a25terminal_control_v1__/`. Verified exact root, directory and symlink constraints before downloading immutable source. Installed disposable test copies of `a25_command_supervisor.py` and `a25_single_dispatcher.py` within that folder only. Existing bridges and services unchanged.

## Method
Created one `SingleDispatcher` instance with **test-only in-memory trusted verifier callbacks** for two simulated registered callers and a disposable owner credential. Exercised authorization under locked/unlocked states, then started a disposable 30-second Python sleep as an A25-managed subprocess on a worker thread and called master `lock()` during execution.

## Observed output
```json
{"locked":"STOP: master command lock engaged","unknown":"STOP: caller authentication failed","bad_owner":"STOP: owner authentication failed","authorized":0,"unlocked_unknown":"STOP: caller authentication failed","active_before_lock":1,"lock":{"locked":true,"failed_to_stop":[],"new_dispatch_blocked":true},"worker_finished":true,"final":{"locked":true,"active":0}}
```

## Evidence classifications
- **VERIFIED:** Within a single dispatcher instance, unauthorized caller denied even while unlocked, authorized caller denied while locked, owner verification required to unlock, authorized command succeeds while unlocked, and master lock cancels an active managed command.
- **UNKNOWN:** Real identity-provider integration, secure credential transport, cross-process exclusive ownership, concurrent ingress behavior, restart/persistent state, durable audit, cancellation of arbitrary child process trees, Android permission model, and whether existing bridges can be bypassed.
- **KNOWN LIMITATION:** The current dispatcher accepts injected verifier callbacks and uses an in-memory supervisor. A caller capable of instantiating its own dispatcher or directly executing scripts bypasses this prototype. It is **not** a running or hardened service.

## Next justified step
Design and test one trusted owner process with authenticated ingress and fail-closed persistent lock state, including concurrent requests and restart behavior. Inventory all legacy entry points before claiming any outsider protection. Keep all phone mutations inside owner-approved test folder; do not replace or restart existing services without separate approval.
