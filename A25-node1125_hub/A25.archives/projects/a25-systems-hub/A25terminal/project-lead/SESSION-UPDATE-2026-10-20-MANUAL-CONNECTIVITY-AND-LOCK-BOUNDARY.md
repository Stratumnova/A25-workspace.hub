# A25terminal — Session Update: Manual Connectivity and Command-Lock Boundary

**Date:** 2026-10-20 (day precision)
**Author:** GPT reporting session; not a claim to the appointed builder or project-lead seat
**Owner:** Zed
**Status:** Owner-stated operating requirements and observed diagnostics; NOT a deployment, implementation acceptance, or new authorization
**Scope:** Documentation only, based on current conversation and read-only GitHub review

## Owner operating clarification — ADOPTED requirement
Zed manually turns the existing Pocket Server bridge and tunnel ON when using remote access and OFF when not. The phone server is intentionally intermittent and designed for cellular network drops and movement. Do not reinterpret temporary unreachability as a failure to be repaired or as a requirement for an always-on supervisor, automatic restarts, new tunnels, or session teardown. Preserve the owner's ability to toggle connectivity and retain his working environment without unnecessary reboot/reconstruction. The command lock is a separate control over incoming remote command dispatch **while connected**; it is not the bridge/tunnel power switch, a local filesystem lock, or an Android-wide lockdown.

## Read-only shutdown observations — VERIFIED for tested interfaces, not universal coverage
- A25 GPT Terminal plugin status and views for a25-test, a25-gpt, a25-bridge, a25-tunnel failed internally. A repeat status check also failed.
- Pocket Gate server_status and read_roundtable failed with MCP connection unavailable; later independent retries also failed.
- Owner-supplied Termux checks initially showed three tmux sessions and a cloudflared process, then later no tmux server on the default socket, no matching tmux/python/uvicorn/cloudflared processes, and curl to 127.0.0.1:8770/mcp returned connection refused / HTTP 000.
- Zed confirmed he manually shut down the services to check closure. Thus this was an intentional OFF-state test, not evidence of an accidental outage. No evidence here establishes that every possible remote endpoint was unreachable; no universal ingress inventory or bypass test was performed.
- Registered ChatGPT tool definitions remained visible while calls failed. Registration is not proof of a live endpoint.
- No terminal commands were sent via plugin; no phone files, services, tunnels, GitHub source, or Roundtable messages were changed by the diagnostic.

## Implications for the new A25terminal command lock
1. Keep **OFFLINE**, **ONLINE+LOCKED**, and **ONLINE+UNLOCKED** as distinct states. Connection failures cannot be presented as a successful password lock.
2. Preserve manual bridge/tunnel toggling and cellular reconnection; do not add uptime or restart management to the lock scope.
3. Enforce the single master lock before any new gateway command dispatch for every caller; authenticate independently even when unlocked. Owner-approved design calls for stopping gateway-managed active commands on lock with verified outcomes, without killing unrelated local jobs.
4. Persist/fail closed as defined in current approved design; no automatic unlock. Ensure reconnection or restart cannot bypass enforcement. Do not assume a lock prototype covers historical bridges.
5. Test the actual new gateway dispatch and its caller boundaries with simulated clients; test connectivity separately from lock enforcement. Avoid treating the historical Gate-02A OAuth work as completed or adopted into the new toolkit.
6. The existing ingress directive and later Command Lock V1 clarification/design must be reconciled by the owner/authorized lead for integration scope; neither document proves deployed protection.

## Current evidence and authority
- **VERIFIED GitHub:** Archives historical intake commit 91712c0e54221a4646a251f20ac9d2d254c2c435 contains A25-POCKET-GATE01-TO-CURRENT-HISTORICAL-NOTES-20261020.md; it labels historical Gate-01, Gate-02, Gate-02A, Shared Space and terminal claims as reference/pending original verification.
- **ADOPTED:** Owner manual ON/OFF operating model and incoming-command rather than local-file lock intent, as stated directly in this conversation; the existing A25terminal approved plan and owner clarifications are separate decision records.
- **HISTORICAL CLAIM:** Earlier terminal mapping and source-only lock prototype reportedly exist, but were not inspected against live phone source in this update.
- **UNKNOWN:** Complete ingress inventory, caller authentication, all bypass paths, deployed lock, runtime continuity after OFF/ON, and actual restart/cancellation behavior.
- **NOT AUTHORIZED by this note:** Phone access, restart, bridge edits, tunnel replacement, deployment, or implementation changes.

## Source links
- [A25terminal README](../README.md)
- [Owner ingress directive](../A25TERMINAL-OWNER-DIRECTIVE-INBOUND-COMMAND-LOCK-20261020.md)
- [Owner Command Lock V1 clarification](OWNER-REQUIREMENTS-2026-10-20-COMMAND-LOCK-V1-CLARIFICATION.md)
- [Command Lock V1 design](COMMAND-LOCK-V1-DESIGN.md)
- [Archives historical intake](../../../A25.office/teams/archives/requests/incoming/A25-POCKET-GATE01-TO-CURRENT-HISTORICAL-NOTES-20261020.md)

## Next justified action
Keep the live environment untouched. When owner-authorized, inspect current ingress routes read-only and reconcile legacy bridge coverage versus new gateway scope, then test the lock within the approved test boundary. No acceptance claim without reproducible gateway and caller tests.
