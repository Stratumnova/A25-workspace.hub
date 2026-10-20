# A25terminal — Manual Command Lock V1 Design

**Owner:** Zed
**Status:** DESIGN PROPOSAL for implementation and testing; not active
**Date:** 2026-10-20
**Basis:** [Owner clarification](OWNER-REQUIREMENTS-2026-10-20-COMMAND-LOCK-V1-CLARIFICATION.md) and [Approved Build Plan V1](../APPROVED-BUILD-PLAN-V1.md)

## Goal and boundary
Prevent curious or accidental command execution through the **new A25 terminal command gateway** when Zed manually locks it. Unlock requires an owner password. This is not Android device locking, not hostile-actor resistance certification, and not a claim that legacy bridges or independent shells are blocked.

## Intended behavior
1. Gateway starts locked unless an explicitly persisted unlocked state has been validated. All gateway command entry points check the same lock before dispatch. Status and secure owner-unlock are the only permitted locked-state actions; status does not reveal secrets.
2. **Owner decision ADOPTED: one master lock, block everything.** On manual `lock`, atomically reject all new gateway command dispatch, cancel/terminate all *A25-gateway-managed* active commands, and report whether each was actually stopped. Do not claim lock completion while an A25-managed command is still running; report any unkillable/stuck command as an explicit failure. Do not indiscriminately kill unrelated Android, Termux, or legacy processes. No per-AI exemptions.
3. Owner supplies password **through a private, no-echo, non-logged local input mechanism**. Do not ask for a password in a ChatGPT message or shell command argument. Do not use a GitHub file or public logs for password storage. Enrollment and recovery must be separate owner actions.
4. Credential verification should use a modern salted password KDF available in the target environment (e.g., scrypt), constant-time verification, restrictive permissions and minimal retained state. A real gateway authentication design and secure credential-entry route must be reviewed before coding a remote unlock interface.
5. Lock state is persisted with atomic writes and defaults to locked on missing, corrupt or inaccessible state. Audit attempts without secrets. No auto-unlock timer or autonomous work.
6. Tests must exercise the **gateway dispatch path**, not merely a helper function: locked command rejected; wrong password rejected; correct password unlocks; command allowed only after unlock; relock blocks; restart persists lock; state corruption fails closed; concurrent requests do not bypass lock; **running A25-managed command canceled and termination verified**; failed cancellation is surfaced rather than silently marked locked.

## Safety and phased delivery
First build a self-contained lock-state and gateway prototype in the authorized disposable folder, using a **test-only password entered locally and never published**. Do not connect it to the existing live bridge, stop services, or collect Zed's real password during prototyping. Security reviews credential handling and gateway integration before promotion. Future bots and Claude/GPT must share the same lock enforcement point.

## Open decisions
- **RESOLVED by owner:** interrupt/cancel A25-managed running commands on lock, rather than letting them finish. Verify termination and report failures.
- Secure owner-facing unlock UI/path and recovery procedure.
- Whether status and other read-only diagnostics remain available while locked.
- Locking legacy command routes requires separate integration; no V1 guarantee until verified.

**Implementation status:** UNKNOWN; design is not deployment authorization.
