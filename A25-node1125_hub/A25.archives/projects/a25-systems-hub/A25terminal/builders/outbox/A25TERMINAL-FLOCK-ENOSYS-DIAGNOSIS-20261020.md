# A25terminal — Android flock ENOSYS Diagnosis

**Date:** 2026-10-20
**Status:** VERIFIED direct operating-system error; deployment HOLD

## Authorized scope
The test was confined to `/storage/emulated/0/Documents/AI_Workshop/terminal tools test folder/__a25terminal_control_v1__/`. The exact root and store were verified to be directories and not symlinks. Created a fresh, disposable `.a25-flock-diagnostic-*.lock` file with `O_EXCL`, attempted a nonblocking exclusive `fcntl.flock`, and closed its file descriptor. No legacy service or terminal bridge was modified.

## Actual observation
```json
{"created_in_authorized_store":true,"flock":"failed","errno":38,"error_name":"ENOSYS","strerror":"Function not implemented"}
```

## Finding
**VERIFIED:** On the tested Android shared-storage location, the nonblocking exclusive `flock` operation fails with errno 38, `ENOSYS` (Function not implemented). This explains why the prior `ExclusiveOwner` prototype could not acquire its first lock. It does not mean another owner process was active.

**UNKNOWN:** Whether any other locking primitive or filesystem is suitable; whether the existing ingress can be routed through one trusted service; real outsider access; full process and restart protection.

## Engineering consequence
The current `a25_exclusive_owner.py` design cannot be used at this location. Do not silently switch to another phone folder or alter service layout: the owner authorized mutations only inside the exact test root. A single-owner architecture requires an alternative that is both supported and verified under the approved boundary, or new explicit authorization for a different deployment path. Preserve original failed test evidence.

**Deployment:** HOLD.
