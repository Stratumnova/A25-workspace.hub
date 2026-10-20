# A25terminal — ZIP Hardening Progress and Blocker

**Status:** IMPLEMENTED IN SOURCE; LIVE RETEST BLOCKED / UNKNOWN
**Owner:** Zed
**Date:** 2026-10-20
**Source:** [a25_file_control.py](../../src/a25_file_control.py)
**Latest hardening commit:** `8400a22d24a7dd8ab2fc6a0161c4c8e674ef2d40`

## Changes
The experimental bounded file control now defines a ZIP entry ceiling (1,000), total declared uncompressed size ceiling (64 MiB), per-member ceiling (16 MiB), and a bounded copy loop for each extracted member. These are code changes, **not** a completed security assessment.

## Verification attempt
A terminal command attempted to fetch the latest GitHub source into a new file under the owner's exact authorized test root, then run hash, extraction and path-escape tests against that new version. The command failed with `AssertionError` at a precondition before the subprocess test cases executed. The precise failed precondition was not isolated. A follow-up diagnostic terminal command was blocked by tool safety checks. No claim is made that the latest revision was deployed, run, or passed.

## Existing verified baseline
The earlier source revision (`3e4c312091c72df5f08f702bcc2fd3a63b9cf415`) passed the reported basic file-operation and ZIP tests; see [previous report](A25TERMINAL-PHASE1-FILE-CONTROL-TEST-20261020.md). Those results do not verify this hardened revision.

## Next justified action
Inspect source and test harness without attempting to bypass a blocked tool action. Establish which assertion failed, ensure exact path safety, and retest the hardened source only through permitted tooling. Do not deploy, alter the bridge, or declare completion before reproducible evidence.

**No secrets or credentials collected. Command lock remains design-only.**
