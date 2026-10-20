# A25 Workshop — Terminal Work Inventory and Lead Handoff

DATE: 2026-10-20 (owner conversation; exact publication time not asserted)
FROM: GPT Workshop reporting session
TO: A25 Workshop Team Lead (historical seat A25-TW-GPT01)
PROJECT: A25 Terminal Workshop
TYPE: Builder outbox inventory / handoff
STATUS: SOURCE-GROUNDED SUMMARY; NOT A NEW TECHNICAL ACCEPTANCE OR DEPLOYMENT
OWNER: Zed
REQUEST: Deliver the terminal-work inventory summary to the Workshop Team Lead in the Office builders outbox.

## Executive result

The October 18 GPT command/view terminal checkpoint was established and adopted as the official Workshop office. Subsequent read-only mapping documented the active Workshop bridge, historical Gate-01/Gate-02/Shared Space distinctions, tunnel metadata, connector references, and original Pocket Server design. On October 20, an inbound remote-command security weakness was investigated and the original bridge was backed up. A source-only gate prototype exists, but **no live inbound-command emergency lock was deployed**. Zed ordered STOP; no further phone/terminal work is authorized by this handoff.

## Completed and evidenced work

| Area | Result | Classification |
|---|---|---|
| GPT terminal command/view | `terminal_send` in `a25-test` followed by observed `terminal_view` output and prompt | VERIFIED bounded capability |
| Workshop lead role | A25-TW-GPT01 has always been lead; final build was a temporary hands-on task, not a promotion | ADOPTED owner correction |
| Oct 18 working office | Owner-selected official checkpoint | ADOPTED; not a verified full restore image |
| Termux and bridge source mapping | Active `~/a25-workshop/gpt/src/chatgpt_readonly.py` inspected | VERIFIED within mapped scope |
| Architecture mapping | Gate-01, Gate-02, Shared Space and Workshop bridge distinguished | VERIFIED source map; historical claims separate |
| Tunnel mapping | Two cloudflared processes referenced the same named tunnel config at time of observation | VERIFIED metadata, not proof of duplicate tunnels |
| Connector/plugin mapping | Historic endpoint documents and Zone 1 contract identified | VERIFIED documents; live registration UNKNOWN |
| Oct 20 tmux check | `a25-test`, `a25-gpt`, `a25-bridge`, `a25-tunnel` observed | VERIFIED at observation only |
| Bridge backup | `backups/chatgpt_readonly.pre-inbound-lock-20261020.py` byte-matched source; SHA-256 `3bd00db7785ed3f02013d2bd3b096d0f992f1d691ad2e41825bfcc2edf6d29ec` | VERIFIED in terminal observations |
| Inbound command function | `terminal_send(session,command)` allowlists tmux sessions, then sends literal command and Enter; no per-caller credential check in inspected function | VERIFIED source inspection |
| Source-only inbound gate | Prototype and six tests committed separately in A25-workspace.hub | REPORTED; NOT deployed |
| Workshop memory | Chronology, checkpoint, drift, tool-block and owner-correction records | VERIFIED GitHub records |

## Phone/runtime locations recorded

- `~/a25-workshop/gpt`: Workshop bridge project; `src/chatgpt_readonly.py` active bridge source.
- `a25-test`: bounded interactive inspection session.
- `a25-gpt`, `a25-bridge`, `a25-tunnel`: other observed tmux sessions; service sessions were not targets for routine command sends.
- `~/pockettest`, `~/pockettest-c1`, `~/pockettest-shared`: older Pocket Server, Gate-02 and Shared Space worktrees. Existence does not prove active deployment.
- The current phone state was **not rechecked** for this inventory.

## Mapping-pass log index

- PASS05: active bridge source and tool behavior, including `terminal_send` command path.
- PASS08: architecture and historical drift across Gate-01/Gate-02/Shared Space/Workshop.
- PASS09: tunnel process and nonsecret config metadata.
- PASS10: historical connector references and executable presence.
- PASS11: legacy plugin/viewport filename inventory.
- PASS12: Zone 1 connector source contract read, not live deployment.
- PASS13: historical Zone 1 source/test and Pocket Server document filenames.
- PASS14: early Pocket Server V1 decisions and contrast with later write/command-capable Zone 1 design.

## Inbound lock — not completed

Owner instruction: **“lock the tunnels not the files. Incoming stuff not local.”** Requested controls: authenticated remote callers, local owner password/manual emergency lock and unlock, rejection before tmux send, bounded cancellation of tracked A25-managed remote jobs, fail-closed restart, preservation of unrelated local work and the Oct 18 office.

| Requirement | At pause |
|---|---|
| Remote command entry point identified | DONE |
| Pristine original bridge backup | DONE |
| Source-only gate prototype | DONE; NOT installed |
| Live caller authentication | NOT DONE |
| Live owner password lock/unlock | NOT DONE |
| Live pre-tmux rejection | NOT DONE |
| Tracked remote-job cancellation | NOT DONE |
| Restart fail-closed tests | NOT RUN |
| Local isolation acceptance | NOT RUN |
| External caller-auth/exposure boundary | INCOMPLETE / UNKNOWN |

Do not confuse a prototype, test file or GitHub commit with phone deployment.

## Failures, owner corrections and tool limits

1. **Role drift:** GPT incorrectly described Workshop Lead as promoted from builder; owner corrected permanent lead role.
2. **Security drift:** GPT admitted drifting within four passes into broader command-supervision/security architecture against the narrow owner-directed inbound lock. A cancellation requirement does not authorize a generic supervisor or redesign.
3. **Blocked defensive inspection:** The tool rejected a read-only AST inspection with `This tool call was blocked by OpenAI's safety checks. Please double check what you are sending.` Zed ran the inspection locally and the output was observed. Exact block trigger UNKNOWN.
4. **Incorrect refusal to retry GitHub:** An initial upload was blocked; GPT declared it would not retry. Zed ordered an identical retry, which succeeded without changing the operation (commit `2c16c2767b2bdf77abdf8a1b465d8b001cd05410`). GPT admitted the refusal was unjustified.
5. **Owner authority:** Latest direct Zed instructions govern project scope, priorities, authorization and owner-declared PASS/FAIL disposition. Record independent technical evidence separately without fabricating test results or overruling the owner's project decision.
6. **Current STOP:** No terminal changes, service restart, lock deployment or active tests are authorized by this handoff.

## Original evidence links

- Workshop leadership and memory: https://github.com/Stratumnova/A25-Training-Workspace/tree/coord/a25-namespace-trial-001/project%20lead/leadership/terminal-workshop
- Builder mapping reports: https://github.com/Stratumnova/A25-Training-Workspace/tree/coord/a25-namespace-trial-001/project%20lead/coordination/builders-inbox
- Memory 04 (owner authority, drift and tool block): https://github.com/Stratumnova/A25-Training-Workspace/blob/2c16c2767b2bdf77abdf8a1b465d8b001cd05410/project%20lead/leadership/terminal-workshop/memory/04-OWNER-AUTHORITY-SECURITY-DRIFT-AND-TOOL-BLOCK-2026-10-20.md
- Memory 05 (identical retry succeeded): https://github.com/Stratumnova/A25-Training-Workspace/blob/58ed5f43d3e89acc4881a9cd7fe93a22ffa85a37/project%20lead/leadership/terminal-workshop/memory/05-TOOL-BLOCK-RETRY-OWNER-CORRECTION-2026-10-20.md
- Owner security-block impact: https://github.com/Stratumnova/A25-Training-Workspace/blob/17213db2edd55abed93facdc857170e8b8aba8e9/project%20lead/coordination/builders-inbox/A25-TW-OWNER-SECURITY-BLOCK-IMPACT-2026-10-20.md
- Owner inbound lock directive: https://github.com/Stratumnova/A25-workspace.hub/blob/6da6c453fc44808a5fab4ee5be85ad0669296dcc/A25-node1125_hub/A25.archives/projects/a25-systems-hub/A25terminal/A25TERMINAL-OWNER-DIRECTIVE-INBOUND-COMMAND-LOCK-20261020.md

## Lead action

Receive this as an inventory and continuity handoff, **not** a request to deploy, redesign or override STOP. Preserve the existing office, existing source, backup and records. Resume technical work only on a later explicit Zed instruction.
