# A25terminal — Incoming Command Gate Source Implementation

**Date:** 2026-10-20
**Owner authorization:** Approved reversible modification and testing of the existing bridge.
**Status:** SOURCE WRITTEN; NOT DEPLOYED; TESTS NOT EXECUTED.

## VERIFIED
- Running `a25-bridge` uses Python module `src.chatgpt_readonly` with MCP `terminal_send(session, command)`, calling `tmux send-keys` for literal input and Enter.
- GitHub contains `src/a25_inbound_gate.py`, a fail-closed in-process admission gate. It defaults locked, requires trusted owner and caller verifier callbacks, and keeps the lock during the trusted send callback.
- GitHub contains `tests/test_a25_inbound_gate.py` with six isolated unit tests. **Presence of tests is not evidence they passed.**
- The live bridge source `src/chatgpt_readonly.py` was not available at the expected project GitHub path. A live source-read operation was blocked by safety checks. No alternate access route was attempted.
- No live tunnel, bridge, Termux service, or local files were modified in this implementation.

## Remaining blockers — do not misrepresent as complete
1. Gate is **not wired** into the live `terminal_send` tool; no live enforcement.
2. Credential-verifier callbacks are injection points only: no real owner-password or remote-caller authentication transport has been integrated.
3. No guarantee every inbound route passes through the gate; bypass inventory incomplete.
4. Lock does not cancel commands already launched by tmux. In-process `inflight` tracks only the send callback, not shell jobs. A25-managed command cancellation still requires separately scoped supervision.
5. Unit tests not executed; no end-to-end test or restart test.
6. A process restart initializes locked, but owner unlock is in-memory only; durable, safe control and operations design remains to be integrated.

## Next implementation requirement
Obtain a verified repository copy of the exact live bridge source through an authorized source-sharing path; integrate the gate before both `tmux send-keys` calls; implement trusted caller and owner verification; run isolated tests; then arrange a controlled reversible live bridge deployment and verify lock/unlock, unknown callers, bypasses, restart, and active-command behavior. Do not expand into local filesystem lockdown.

## Evidence classifications
- **ADOPTED:** Owner directive is inbound remote command lock, not local file protection.
- **VERIFIED:** Gate and tests committed to GitHub, live bridge's `terminal_send` ingress previously inspected.
- **UNKNOWN:** End-to-end protection and complete ingress coverage.
- **NOT VERIFIED:** Tests passing or deployed master lock.
