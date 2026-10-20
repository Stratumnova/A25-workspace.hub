# A25terminal — Cross-Caller Locked-State Test

**Date:** 2026-10-20
**Status:** VERIFIED uniform rejection of simulated concurrent gateway calls; external caller authorization and ingress protection UNKNOWN
**Source:** Gateway prototype `a8402bdf733e6486d4c72cd950f592158c9053a6`

## Owner directive
One master lock must block commands from all callers, including outsiders, not just Zed/GPT/Claude. Test caller authorization and bypass resistance separately; never infer full external security from a local simulated test.

## Live test
Using existing terminal transport to execute the *new gateway prototype* inside `/storage/emulated/0/Documents/AI_Workshop/terminal tools test folder/__a25terminal_control_v1__/`, verified exact authorized root, launched seven simultaneous subprocess invocations of `run list`. Labels in the test harness: owner, GPT, Claude, bot, unknown, unauthenticated, second-session. All seven returned exit code 1 and `STOP: master command lock engaged`. `status` returned `locked: true`. A further `run delete` attempt was rejected and the disposable test target remained intact.

## Evidence interpretation
**VERIFIED:** Uniform locked-state rejection across seven concurrent subprocess requests to the gateway.
**NOT VERIFIED:** Caller identity authenticity, outsider network ingress, unlock attempts by genuinely unauthenticated principals, access control when unlocked, or ability to bypass the gateway using existing terminal bridge/direct Termux. The labels were *simulated metadata*, not authenticated identities. No external parties or networks were probed.
**KNOWN GAP:** Current prototype lacks active-command cancellation and cross-process coordination. The existing legacy bridge remains outside its lock.

## Next tests
Introduce a gateway-owned cross-process serialization and active-command cancellation mechanism. Separately inventory exposed command entry points and prove unauthorized callers cannot reach an unlocked dispatch path. Keep all mutation/testing within owner-approved folder and preserve existing services.
