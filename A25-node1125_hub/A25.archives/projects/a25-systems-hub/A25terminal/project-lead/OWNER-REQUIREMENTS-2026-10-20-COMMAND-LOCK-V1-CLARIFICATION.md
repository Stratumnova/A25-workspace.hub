# A25terminal — Owner Clarification: Command Lock V1

**Owner:** Zed
**Status:** ADOPTED requirement clarification; implementation and enforcement UNKNOWN
**Date:** 2026-10-20
**Related:** [Earlier requirement record](OWNER-REQUIREMENTS-2026-10-20-TEST-BOUNDARY-AND-LOCKDOWN.md), [Approved Build Plan V1](../APPROVED-BUILD-PLAN-V1.md)

## Clarified owner intent

The earlier phrase "lock the system" was overbroad. Zed clarified that he wants to **lock all commands issued through A25 terminal controls, and unlock them with a password** when he returns. This is a small, manual safety feature against accidental or curious use while he is away, not an Android-wide device lockdown and not a replacement for Security's work against malicious bypass.

## V1 behavior to build and test

- Owner-invoked **lock** prevents command execution through the new A25 terminal control gateway for GPT, Claude, and future authorized callers alike.
- Owner-invoked **unlock** requires secure password verification. Passwords must not appear in public GitHub, ChatGPT transcripts, shell command strings, logs or receipts; design a secure input path before implementation.
- A limited **lock-status** operation can report locked/unlocked without executing arbitrary commands or revealing secrets.
- Audit state changes and failed unlock attempts without capturing secrets. Deny by default if state cannot be read reliably.
- Lock applies to **all command entry points managed by the new gateway**, not just a particular AI identity. Existing historical bridges or local shells are outside V1 enforcement until explicitly integrated; do not claim they are blocked.
- Preserve a documented owner-only local recovery method and avoid disabling the working development connection.
- No automatic timers, scheduled actions, autonomous work, package installations or service modifications are authorized by this clarification.
- Determine and test behavior for already-running commands and sessions before claiming full command lock.

## Evidence and relationship to earlier note

This is a **later owner clarification** and **SUPERSEDES the earlier device-wide lockdown interpretation** in the linked requirements record. The original text remains preserved for traceability. The approved V1 plan remains unchanged; this note adds a scoped feature requirement. Implement and test the new control itself, using the owner's separately authorized file-operation test boundary where appropriate. Security retains responsibility for hostile-threat hardening.

**Implementation:** UNKNOWN / not yet performed.
