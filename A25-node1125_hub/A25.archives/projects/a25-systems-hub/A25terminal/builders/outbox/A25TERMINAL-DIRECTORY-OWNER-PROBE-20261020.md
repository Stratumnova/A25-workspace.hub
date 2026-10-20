# A25terminal — Directory Owner Probe

**Date:** 2026-10-20
**Status:** VERIFIED filesystem primitive, NOT verified security boundary
**Deployment:** HOLD

## Scope
All phone mutations confined to `/storage/emulated/0/Documents/AI_Workshop/terminal tools test folder/__a25terminal_control_v1__/`. Root and store were checked for directory identity and symlink avoidance. A fresh unique `.a25-owner-mkdir-probe-*` directory was created and preserved. No existing service, tmux session, bridge or credentials modified.

## Direct observation
```json
{"first_mkdir":"acquired","second_mkdir":"denied_exists","directory_present":true}
```

**VERIFIED:** First `Path.mkdir` succeeded, second `Path.mkdir` of identical name raised `FileExistsError`, and the marker directory remained present. Unlike `flock`, directory creation is available on the tested storage.

## Prototype
Source-only `src/a25_directory_owner.py`, commit `033297537aa2e1ca03b373b62a10078d6ea2f00d`, implements a test-only fail-closed marker. Existing marker rejects new startup; `release()` intentionally never removes it.

## Limitations
**UNKNOWN:** Two-process concurrent create race outcome, crash/restart recovery, whether arbitrary callers can remove markers, whether the filesystem provides suitable ownership guarantees, and integration with the dispatcher.

**KNOWN:** A persistent directory marker is not proof of a live owner and may deny startup forever after a crash. It is not a credential, IPC service, or security boundary. Do not use it to declare the terminal secured or to bypass current ingress.

## Next
Run isolated simultaneous-process creation tests and design authenticated single-owner ingress. Maintain deployment hold and preserve markers as evidence.
