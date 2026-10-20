# A25 Systems Hub — Terminal Control Toolkit Component Build Request

**Record status:** PROPOSED DRAFT — Workshop Lead review and Archives staging; NOT owner-approved implementation
**Prepared by:** GPT Workshop Builder, for Workshop Lead
**Owner:** Zed
**Project:** A25 Systems Hub
**Document class:** Component build proposal / draft work request (not a formal issued WO)
**Creation date:** 2026-10-20 (system date; exact UTC timestamp not established for formal record naming)
**Time source:** conversation system date; Archives to supply actual UTC creation timestamp at publication
**Canonical repository:** `Stratumnova/A25-workspace.hub`, branch `main`
**Proposal staging home:** `A25-node1125_hub/A25.archives/projects/a25-systems-hub/build-requests/`
**Proposed permanent component home, after owner approval:** `A25-node1125_hub/A25.archives/projects/a25-systems-hub/A25terminal/`
**Authority:** Proposal only. Archives and Workshop Lead will handle formal filing, component README/onboarding, approvals and subsequent orders. No source implementation, package installation, service changes or phone deployment authorized by this draft.

## 1. Goal and owner interaction

Build one coherent A25 terminal and workstation toolkit so the owner can direct GPT in ChatGPT by ordinary messages, and GPT can execute the requested terminal, file, process, project, maintenance and recovery operations on the owner's behalf. Claude should have its own authenticated connection to the same controlled capabilities. Later the Workstation Assistant, Archives Bot and Security Bot may use suitable tools under their respective owner-authorized roles.

The owner does not need to enter commands in Termux. The system must not initiate work autonomously, on schedules, from monitors, or through API-triggered automatic workflows. An explicitly requested action may involve a bounded sequence of commands and ordinary subprocesses necessary to complete that action; this is execution of a requested task, not autonomous task initiation.

**Capability objective:** full, practical terminal functionality for owner-directed GPT/Claude work, rather than a four-command allowlist or read-only tmux viewport. Do not impose an arbitrary small command catalog. Authentication, caller attribution, scope, confirmations for high-impact operations, isolation of private material, evidence logging and emergency recovery remain required. These are safeguards, not a policy of making the AI unable to carry out legitimate owner requests.

## 2. Current project fit and source boundaries

- Parent: `A25.archives/projects/a25-systems-hub/` — canonical Systems Hub project.
- Existing sibling `A25chatroom/` owns messaging and its source/history. Terminal controls are a separate component, not a Chatroom subfolder.
- Existing sibling `main build/` is for integration of independently tested and approved components, not their development home.
- `build-requests/` holds proposals until the owner approves an identified version; originals remain preserved.
- Office (`A25.office/teams/workshop/`) handles formal assignments and reports, linking to the component's substantive history.
- The original Pocket Server, Gate and Zone 1 code and historical repositories are REFERENCE; do not silently adopt, modify or migrate them. Existing live services remain untouched until separately authorized.

## 3. Requested component structure

The following is a **proposed functional tree**, not an instruction to create every directory immediately. Archives should create the approved minimal landing and team exchange structure consistent with the existing Chatroom component. Source directories appear only as actual implementation begins. Component path and names are proposals for owner approval.

```text
A25-node1125_hub/
└── A25.archives/
    └── projects/
        └── a25-systems-hub/
            ├── build-requests/
            │   └── [dated Archives-staged Terminal Control Toolkit proposal].md
            ├── A25chatroom/                 # existing; unchanged
            ├── main build/                  # existing integration room; unchanged
            └── A25terminal/                 # proposed permanent sibling component
                ├── README.md               # Archives-owned landing/navigation
                ├── ONBOARDING.md            # Archives-owned operating/recovery guide
                ├── project-lead/            # lead plans, scope and decisions
                ├── builders/
                │   ├── inbox/               # scoped assignments
                │   └── outbox/              # results and execution evidence
                ├── archives/
                │   ├── inbox/
                │   └── outbox/
                ├── security/
                │   ├── inbox/
                │   └── outbox/
                ├── src/                     # when implementation authorized
                │   ├── a25_terminal/
                │   │   ├── bridge/           # GPT, Claude and future bot tool adapters
                │   │   ├── identity/         # authenticated caller identity and grants
                │   │   ├── execution/        # PTY, commands, subprocess, timeouts
                │   │   ├── sessions/         # tmux/session lifecycle and attach/view
                │   │   ├── services/         # named A25 service registry and controls
                │   │   ├── processes/        # process discovery, pause/freeze/stop
                │   │   ├── files/            # read/write/search/tree/diff/patch
                │   │   ├── projects/         # git, repo checks, test/build helpers
                │   │   ├── backup/           # snapshots, restore and integrity
                │   │   ├── diagnostics/      # health, ports, logs, environment
                │   │   ├── audit/            # execution receipts and provenance
                │   │   └── control/          # owner-invoked pause/stop/emergency
                │   ├── cli/                  # local a25-* commands and recovery entry
                │   └── packaging/            # Termux setup/config and deployment assets
                ├── tests/                   # unit, integration, failure, recovery
                ├── fixtures/                # disposable test data only
                ├── docs/                    # tool contract and technical specifications
                └── releases/                # approved manifests, hashes, ZIP receipts
```

**Do not put** runtime secrets, actual tokens, private logs, databases, live credentials or personal files in the public GitHub tree. Use Termux-private runtime paths and documented backup/redaction rules. A ZIP is a packaging artifact, not a new project home. Keep the component source, tests and fixes in `A25terminal/` permanently.

## 4. Tool families and requirements

### A. Owner command gateway and execution
- Receive an explicit task through the GPT/Claude connection; identify the actual authenticated principal, task initiator, target and approval context. No reliance on a model's self-claimed name.
- Execute general shell commands and multi-step tasks with working directory, environment, stdin, stdout/stderr, exit code, signal, timeout, cancellation and explicit result receipts.
- Support one-shot commands and persistent interactive PTY/tmux sessions; show live output and terminal history within privacy rules.
- Provide owner-requested elevated/destructive operations through explicit confirmation and appropriate device permission, not arbitrary command-name restrictions.
- Support concurrent independent GPT/Claude sessions with resource accounting, clear ownership and collision protection for shared files.

### B. Status, discovery and diagnostics
- `a25-status`: unified view of registered A25 services, tmux sessions, process IDs, health and last known action.
- `a25-tree`, `a25-find`, `a25-inspect`: locate directories, enumerate filenames, inspect permissions/metadata and search within authorized locations.
- `a25-processes`, `a25-ports`, `a25-health`, `a25-logs`: inspect processes, listeners, endpoint health and bounded/redacted logs.
- Capture package inventory, Termux/Android versions, storage permissions, available disk/memory and relevant tool versions on explicit request.

### C. Owner-invoked service and process controls
- `a25-pause-all`: refuse new A25 work while allowing current operations to finish; define exact affected services and exceptions.
- `a25-resume-all`: re-enable owner-requested work.
- `a25-freeze TARGET` / `a25-thaw TARGET`: suspend/resume an identified A25-managed process group where technically safe; never freeze the sole recovery path or command transport.
- `a25-stop TARGET`, `a25-stop-all`: graceful shutdown, bounded wait, report any survivors; owner can select whether the terminal bridge and tunnel are included.
- `a25-start TARGET`, `a25-start-all`, `a25-restart TARGET`: manual lifecycle actions for registered services only.
- `a25-emergency-stop`: explicit owner-invoked, local recovery-capable escalation for identified A25-managed processes; avoid indiscriminate `pkill` or terminating all Termux/Android processes.
- `a25-disable TARGET` / `a25-enable TARGET`: change manual startup eligibility or any already-existing startup registration only with explicit owner authorization; no new automatic startup mechanism by default.
- Support an independent local recovery path if remote connectivity is lost. Define the shutdown ordering so the bridge is not killed before requested work can report results, except in a genuine local emergency.

### D. Files, source and development
- List/tree/find/search/read/create/edit/rename/move/copy/delete with before/after evidence, content-size handling and safe handling of symlinks/path traversal.
- Atomic file replacement where practical; revision checks or locking for GPT/Claude concurrent edits; previews and diffs for consequential changes.
- Git status, diff, branch/commit inspection, fetch and authorized commit/push on the official repo and main branch only; never create new branches or repos without owner approval.
- Run Python, shell, tests, linters and build commands as explicitly requested; capture exit codes and actual output; distinguish source checks from live deployment.
- Archive/ZIP, hashes, manifests, checksums and selective copy/restore for owner-requested transfers.

### E. Backup, audit and recovery
- Manual snapshot, integrity verification, compare, restore preview and owner-confirmed restore.
- Append-only or tamper-evident local receipts: request ID, actual principal, initiating owner/AI, command, target, start/end, exit status, files changed, and redaction markers.
- Record failures and incomplete operations; do not label tests PASS without observed execution.
- Recovery commands must work without Chatroom or an external tunnel, with secrets stored separately.
- No periodic monitoring, automatic repair, unattended backup or autonomous retry unless Zed later changes the operating rule explicitly.

### F. Future bot access
- Workstation Assistant Bot: document and template operations with authorized draft storage.
- Archives Bot: navigation, indexing, source references and authorized records operations.
- Security Bot: inspect change receipts, process/service events, hashes and coverage gaps; write security reports only when authorized.
- Bots do not inherit owner authority or execute independently; tool requests require explicit initiating instruction and authenticated role attribution.

## 5. Termux software inventory and installation candidates

**Inspect before installing**; existing installation and versions are not assumed from historical notes. Proposed reusable components:

| Candidate | Purpose | Deployment rule |
|---|---|---|
| `tmux` | persistent independent interactive sessions | inspect existing session manager; reuse if suitable |
| `termux-services` / runit | named A25 service lifecycle, status and supervised execution | evaluate carefully; do not enable unattended startup/restart by default; reconcile existing process ownership |
| `procps` | process discovery, signals and process groups | install only if missing |
| `coreutils`, `findutils`, `grep`, `sed`, `tar` | filesystem, search and packaging | reuse existing |
| `git`, `openssh`, `curl` | source control, secure transfer, diagnostics | verify existing setup; do not expose credentials |
| `jq` | inspect structured JSON output and receipts | useful addition |
| `sqlite` | optional structured local audit metadata | Termux-private location, not public GitHub |
| `rsync` | efficient manually initiated backups and copies | useful addition |
| Python and appropriate PTY/bridge libraries | tool server, terminal sessions, test harness | preserve working Python environment; avoid unplanned upgrades |
| `Termux:API` | optional Android notifications and device integration | not required for initial toolkit; no autonomous triggers |

Evaluate Termux-specific compatibility, package versions, Android storage access, wake locks, service supervision semantics and command transport before choosing installation commands. Existing A25 terminal plugin historically offered status/view and now has a command-sending action, but this is not proof that the future toolkit or authentication design exists.

## 6. Build phases and measurable acceptance

**Phase 0 — Discovery and design (read-only, separately ordered):** Inventory actual Termux paths, processes, current service start methods, package versions, tmux sessions, bridges/tunnels and existing recovery paths. Identify A25-managed processes versus unrelated workloads. Confirm component interfaces with Systems Hub and Security. Produce verified inventory and dependency decisions.

**Phase 1 — Local toolkit foundation:** Implement `a25-status`, discovery, tree/search, process/session inspection, logs, explicit task receipts, and local manual CLI. Tests must demonstrate real exit codes, error handling and no mutation in read-only operations.

**Phase 2 — General command and file execution:** Build authenticated GPT/Claude bridge, interactive PTY/tmux, multi-step command execution, cancellation, file changes, Git/test helpers and concurrent-edit protection. Verify both principals separately with actual commands and shared-file lifecycle tests. No substitute read-only viewport.

**Phase 3 — Owner lifecycle controls:** Register selected A25 services, then implement pause/resume, freeze/thaw, start/stop, stop-all and emergency-stop. Test first on disposable dummy services, then approved A25 targets. Verify tunnel-loss recovery, survivors reporting, protected recovery channel and no impact on unrelated processes.

**Phase 4 — Backup, integrity and audit:** Owner-invoked snapshots, hashes, diff, restore previews and restores, command receipts and coverage-gap reporting. Verify a complete disposable backup/restore round trip.

**Phase 5 — Bot-compatible interfaces:** Expose scoped capabilities for the three future bots when each bot is separately authorized. Verify attribution, owner-initiated task requirement and access boundaries; no autonomous bot action.

**Phase 6 — Systems Hub integration:** Integrate only an approved, independently tested version through `main build/`; record source commit, package hash, dependency versions, Security review, test receipts, rollback, recovery and owner cutover decision. Do not move component source. Do not disturb historical Pocket Server until explicit authorization.

## 7. Acceptance conditions and safety/failure tests

1. Owner can request a command in GPT chat and receive the actual terminal stdout, stderr and exit status.
2. GPT and Claude independently authenticate and operate authorized terminal sessions; attribution cannot be spoofed by text prompts.
3. The toolkit handles arbitrary legitimate owner-requested shell workflows, including interactive commands, without a four-action limitation.
4. `pause-all` rejects new A25 work but preserves recovery and properly accounts for in-flight tasks.
5. `stop-all` affects only explicitly registered A25 services; reports each outcome; preserves a usable local recovery path.
6. `freeze/thaw` cannot strand the only bridge or lock out recovery.
7. Emergency stop is available locally after loss of tunnel/server connection.
8. Concurrent file writes detect collisions; Git changes are inspectable and reversible where feasible.
9. A backup can be verified and restored from disposable data; secrets are not written to public GitHub.
10. Audit receipts distinguish actual observed command execution, reported claims and unknowns; missing monitoring coverage is visible.
11. No command, backup, monitoring, repair, restart or bot task begins autonomously or from a scheduled/API-triggered workflow.
12. Failure injection covers command timeout, cancelled command, disconnected client, partial service shutdown, inaccessible storage and corrupted snapshot.

## 8. Dependencies, decisions and risks for owner/Archives/Security

- **Owner decision:** confirm component name/path (`A25terminal/`) and exact owner-confirmation thresholds for destructive commands.
- **Archives:** stage this proposal under `build-requests/`, preserve original, create approved component landing only after decision, supply guides/README/onboarding and record metadata; maintain canonical history and links.
- **Workshop Lead:** set actual phase scope and issue builder assignments after approvals. This draft is not an instruction for builder execution.
- **Security:** review authentication, permissions, command transport, audit redaction, privilege escalation, local recovery and impact of `termux-services` supervision. Full terminal capability increases consequence of credential compromise; separate identities and verifiable owner delegation are critical.
- **Integration:** coordinate with Chatroom and Systems Hub without treating message access as terminal command authority. GPT-platform messages are the owner's interaction channel; connection adapters may use APIs as transport, but **not as autonomous triggers for work**.
- **Operational risks:** Android background execution restrictions; Termux storage permissions; service restart semantics; process group handling; accidental bridge termination; duplicate managers; shared-file races; public repository exposure; untested package upgrades; backups of secrets.

## 9. Requested action — Archives staging only

Archives and the Workshop Lead are requested to:

1. Preserve this draft as the identifiable original proposal and give it a charter-compliant actual UTC record ID/time on publication.
2. Stage the proposal in the existing `a25-systems-hub/build-requests/` area on the existing repository `main` branch, subject to the owner's instructions and Archives permissions.
3. Review and, when authorized, establish the permanent sibling component `A25terminal/` with appropriate component README/onboarding and team exchange rooms; do not create unrelated or speculative folders.
4. Return the proposed/approved exact path and any owner decisions to the Workshop Lead. Implementation begins only after a separate scoped work order and applicable reviews.

**Explicitly out of scope now:** code edits, package installation, terminal commands, phone storage changes, process/service actions, tunnel or bridge changes, autonomous jobs, new GitHub branches/repos, and changes to historical repositories.

## 10. Governing sources reviewed

- [Node 11 root charter](https://github.com/Stratumnova/A25-workspace.hub/blob/main/A25-node1125_hub/README.md)
- [Workshop operating boundaries](https://github.com/Stratumnova/A25-workspace.hub/blob/main/A25-node1125_hub/A25.office/teams/workshop/lead/rules/README.md)
- [Systems Hub project](https://github.com/Stratumnova/A25-workspace.hub/blob/main/A25-node1125_hub/A25.archives/projects/a25-systems-hub/README.md)
- [Systems Hub onboarding](https://github.com/Stratumnova/A25-workspace.hub/blob/main/A25-node1125_hub/A25.archives/projects/a25-systems-hub/ONBOARDING.md)
- [Component build requests rules](https://github.com/Stratumnova/A25-workspace.hub/blob/main/A25-node1125_hub/A25.archives/projects/a25-systems-hub/build-requests/README.md)
- [Chatroom component onboarding](https://github.com/Stratumnova/A25-workspace.hub/blob/main/A25-node1125_hub/A25.archives/projects/a25-systems-hub/A25chatroom/ONBOARDING.md)
- [Main build integration rules](https://github.com/Stratumnova/A25-workspace.hub/blob/main/A25-node1125_hub/A25.archives/projects/a25-systems-hub/main%20build/README.md)
- [Existing Systems Hub Workshop request](https://github.com/Stratumnova/A25-workspace.hub/blob/main/A25-node1125_hub/A25.office/teams/workshop/requests/incoming/A25-SYSTEMS-HUB-WK-WR-20261020T020916Z.md)

**Evidence classification:** Repo rules and project paths were directly inspected. This toolkit design, candidate software, proposed path and acceptance tests are PROPOSED, not built, installed, verified or adopted.