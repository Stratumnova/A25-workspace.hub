# A25terminal — IPC Filesystem Capability Probe

**Date:** 2026-10-20
**Status:** VERIFIED socket bind failure; authenticated IPC not implemented
**Deployment:** HOLD

## Scope
Android phone checks confined to `/storage/emulated/0/Documents/AI_Workshop/terminal tools test folder/__a25terminal_control_v1__/`. Verified exact authorized root and store are directories and not symlinks. No listener was left running; socket objects were closed. Existing tmux sessions, bridge, and tunnel were not changed.

## Tests
1. Attempted `socket.AF_UNIX` filesystem bind using a unique absolute path in the authorized store. Failed; initial exception recording lacked errno.
2. Attempted another fresh unique short relative socket name after setting current directory to the authorized store. This removes the full pathname-length issue. Recorded:
```json
{"absolute_path_length":109,"relative_name":".ipc-f7b5a728","bind":"failed","errno":13,"error_type":"PermissionError","error_repr":"PermissionError(13, 'Permission denied')"}
```

## Findings
**VERIFIED:** Unix-domain filesystem socket bind at the tested location fails with permission denied, even with a short relative name. No authenticated IPC server was established.

**UNKNOWN:** Whether any other transport can satisfy authentication, single-owner routing, filesystem boundary, and fail-closed startup. The original full path length could also have contributed to its failure, but does not explain the short-name permission denial.

## Engineering decision
Do not silently relocate a socket outside the authorized folder, create an abstract namespace listener, start a TCP listener, or modify legacy services without an explicit approved transport design and test scope. Continue source-only architecture design, with credentials never in arguments/logs, one owner, and all command ingress routed through that owner. No claim that current terminal is secured.

**Deployment:** HOLD.
