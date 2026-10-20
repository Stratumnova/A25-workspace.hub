# A25terminal — Caller Authentication Live Test

**Date:** 2026-10-20
**Source commit:** `31c4bab381f0a7c435e5322e0c0b447fcd58d771`
**Source SHA-256:** `483e99a277c08009a68c2f02092e44d147071e0c6a79aaf989d1b2b10a14fa21`
**Status:** VERIFIED isolated decision tests; NOT production-ready

## Background and independent review
Claude reported that the earlier prototype, when isolated and unlocked, executed a dummy `run list` for an unidentified caller. The reported output `CONTROL_EXECUTED_FOR_CALLER: NONE` is a **HISTORICAL CLAIM** supported by the owner's supplied transcript/screenshots. GPT separately inspected the source and confirmed the absence of per-call caller authentication. This finding motivated the new check.

## New implementation
The gateway now requires a registered caller id and a separate credential for `run`; scrypt derives a digest from the no-echo secret, verified with `hmac.compare_digest`. Unknown and missing callers fail closed. The global lock is a separate additional gate. The test-only registry is stored inside the owner's authorized test folder. No caller secret was placed in GitHub or passed as a command argument.

## Live Android test
Within `/storage/emulated/0/Documents/AI_Workshop/terminal tools test folder/__a25terminal_control_v1__/`, downloaded the immutable source revision, loaded the gateway with an **isolated disposable registry** and in-memory random credential, and exercised `run(["list"], caller=...)` while simulating both lock states without changing the existing live lock.

Observed:
- Unknown caller while unlocked: `STOP: caller authentication failed`.
- Missing caller while unlocked: `STOP: caller authentication required`.
- Registered caller with wrong credential while unlocked: `STOP: caller authentication failed`.
- Registered caller with correct credential while unlocked: **ALLOWED**; actual file control produced read-only directory listing.
- Registered caller with correct credential while locked: `STOP: master command lock engaged`.
- Isolated test caller registry deleted afterward; existing live gateway lock and credential files unchanged by this test.

## Limitations / UNKNOWN
This test monkeypatched the gateway's `state()` and `getpass.getpass()` in memory to isolate authentication decisions. It did **not** test actual remote authentication, secure secret delivery, concurrent cross-process dispatch, active command cancellation, audit durability, or bridge bypass. The caller id itself is public and not an authentication factor. On-device shared storage may not enforce Unix-style file permissions; credential storage and ingress need Security review. The original gateway and legacy terminal services remain separate and unaffected.

## Next
Implement serialized dispatch and reliable cancellation for A25-managed commands; add durable audit and secure credential entry appropriate to actual caller transport; test end-to-end with no simulated state before production integration.
