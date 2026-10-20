# A25terminal — Live Incoming Command Path Inspection

**Date:** 2026-10-20
**Scope:** READ-ONLY live bridge/tunnel inspection, no service changes
**Owner directive:** Lock incoming remote commands through tunnel/bridge; do not lock local files or local Termux usage.

## VERIFIED on the running Android phone
- tmux session `a25-bridge` contains a Python process, PID 6882 at inspection, invoked with `-m src.chatgpt_readonly`.
- tmux session `a25-tunnel` contains `cloudflared`, PID 6965 at inspection.
- tmux session `a25-gpt` exists.
- The bridge process working directory is `/data/data/com.termux/files/home/a25-workshop/gpt`.
- Its module `src/chatgpt_readonly.py` defines MCP tools `terminal_status`, `terminal_view`, and `terminal_send`.
- The `terminal_send(session, command)` function contains a session allowlist check and invokes `tmux send-keys -t <session> -l <command>` then `tmux send-keys -t <session> Enter`.
- No lock check was verified in the inspected `terminal_send` branch conditions; observed conditions included `session not in allowed` and `result.returncode != 0`.

## Finding
**VERIFIED:** The running bridge has an incoming remote terminal-input capability through the MCP `terminal_send` tool. A manual master lock must reject incoming commands **before** either `tmux send-keys` call. Locking local files or merely protecting a different dispatcher does not meet the owner's objective.

**UNKNOWN:** All other command-capable routes, tunnel configuration/authentication, other MCP services, remote caller identity enforcement, active command cancellation semantics, and whether any alternate endpoint bypasses this bridge.

## Correct implementation order
1. Identify all externally reachable command/input entry points, especially bridge tools and tunnel routes.
2. Implement one manually password-controlled inbound gate at those entry points. Locked must reject new command/input requests before any tmux write. Even when unlocked, authenticate each caller. No secrets in CLI arguments, logs, or GitHub.
3. On lock, stop only A25-managed remote commands and report survivors. Do not terminate unrelated local Termux jobs or local phone use.
4. Restart fail-closed. Test locked denial, authorized unlock, unknown caller rejection, in-flight cancellation, bypass paths, and restart.
5. Keep existing services unchanged until owner separately approves a specific reversible deployment.

**Deployment:** NOT PERFORMED. This report is evidence and a narrow design target, not a claim of protection.
