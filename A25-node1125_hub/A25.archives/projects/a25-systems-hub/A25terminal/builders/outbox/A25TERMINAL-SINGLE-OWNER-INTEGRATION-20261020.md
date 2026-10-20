# A25terminal — Single-Owner Integration Test

**Date:** 2026-10-20
**Status:** VERIFIED isolated integration PASS; production deployment HOLD

## Sources
Single-owner composition: `src/a25_single_owner_service.py`, commit `7f3d888620acdb9f86e092c7d5941b47c43b1d03`.
Directory owner: `src/a25_directory_owner.py`, commit `033297537aa2e1ca03b373b62a10078d6ea2f00d`.
Other dependencies: existing `a25_persistent_dispatcher.py`, `a25_persistent_lock.py`, `a25_command_supervisor.py`.

## Dependency correction
Read-only inventory confirmed `a25_directory_owner.py` absent from the authorized test store, while the three dispatcher dependencies and the single-owner service test copy existed. Downloaded the directory-owner source at the pinned commit and created ONLY the absent `a25_directory_owner.py` using exclusive create mode `xb`. No existing source or test artifacts overwritten.

## Authorized test scope
All Android test mutations inside `/storage/emulated/0/Documents/AI_Workshop/terminal tools test folder/__a25terminal_control_v1__/`. Verified exact root and store directories and absence of symlink redirection. Used fresh unique owner marker and state file. Disposable callback credentials only; no real secrets. Existing bridge/tmux services unchanged.

## Actual observed result
```json
{"initial":{"locked":true,"active":0},"second_owner":"denied","locked_run":"denied","unlocked":{"locked":false,"active":0},"authorized_exit":0,"unknown":"denied","close":{"locked":true,"failed_to_stop":[],"new_dispatch_blocked":true},"final":{"locked":true,"active":0},"marker_remains":true}
```

## Classification
**VERIFIED:** One service started locked; a second service construction against the same marker was denied; command while locked denied; owner unlock succeeded; authenticated benign command exited zero; unknown caller denied; close locked and reported zero active commands; marker preserved.

**UNKNOWN:** Independent-process authenticated ingress, real credential transport, crash recovery, direct bypass prevention, uncooperative marker deletion, production isolation, and full multi-caller integration. The marker is fail-closed but can leave stale startup denial.

**Decision:** Do not deploy. Build and verify an authenticated single-owner IPC entry point and crash/restart procedure, without modifying legacy bridges unless separately authorized.
