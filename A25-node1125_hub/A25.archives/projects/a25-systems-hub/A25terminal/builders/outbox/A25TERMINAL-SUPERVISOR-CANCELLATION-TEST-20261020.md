# A25terminal — Supervisor Cancellation Test

**Status:** VERIFIED isolated in-process behavior; cross-process and production integration UNKNOWN
**Source revision:** `71614328e2f0a084eeae228001baecbd47acb63d`
**Scope:** `/storage/emulated/0/Documents/AI_Workshop/terminal tools test folder/__a25terminal_control_v1__/`

## Source and method
Retrieved the new `src/a25_command_supervisor.py` by immutable GitHub commit and saved as `a25_command_supervisor_test.py` within the authorized Android test folder. Verified the exact root and contained destination. Created one in-process `CommandSupervisor`, executed negative authorization tests, then launched a disposable 30-second Python sleep through its `dispatch` method on a worker thread. Called `lock()` while the subprocess was active.

## Observed output
```json
{"locked_reject": true, "unauthorized_unlock_reject": true, "unauthorized_run_reject": true, "tracked_active": true, "lock_result": {"locked": true, "failed_to_stop": [], "new_dispatch_blocked": true}, "thread_finished": true, "final_status": {"locked": true, "active": 0}}
```

## Findings
- **VERIFIED:** Default lock denies authorized dispatch; unverified unlock rejected; unauthenticated dispatch rejected when unlocked.
- **VERIFIED:** Active managed disposable subprocess was tracked and stopped by `lock()`; worker thread finished; final active count 0.
- **UNKNOWN:** Cross-process caller coordination, malicious command escaping its process group, cancellation under SIGTERM/SIGKILL resistance, state persistence/restart, and safe integration with real gateway.
- **KNOWN:** This is a library component, not a listener, authentication system or installed terminal bridge. Every caller must share a single supervisor owner; separate instances do not share locks. Existing services untouched.

## Next
Build a single-owner authenticated gateway service or equivalent trusted dispatcher that routes all caller requests through one supervisor; test concurrent callers and restart behavior before any production integration. Do not claim outside users are excluded from legacy bridges.
