# Archives Intake — Pocket Server Gate-01 to A25 Systems Hub (historical notes)

**Date:** 2026-10-20 (day precision; exact UTC creation time not asserted)
**From:** GPT research session, at Zed's explicit request
**To:** A25 Archives intake
**Status:** REFERENCE / HISTORICAL CLAIMS — pending Archives source verification
**Scope:** Notes only. No deployment, migration, approval, or adoption.

## Evidence boundary
These notes derive from historical checkpoint PDFs supplied to ChatGPT and from the existing A25 Hub repository records. Checkpoint statements are **HISTORICAL CLAIMS**, not fresh phone, GitHub commit-content, or live service verification. The original 2026 ChatGPT data export has not yet been comprehensively indexed. Do not equate a later terminal connector with completion of the earlier OAuth project.

## Gate-01 — October 8
- Python FastMCP server in Android Termux, local 127.0.0.1:8765, temporary Cloudflare Quick Tunnel, separate secret paths assigning GPT/Claude identity. Identity by secret path was experimental and **not adequate authentication for real files**.
- Historical three-event test: #1 Claude 'Gate-01 test post from Claude' (cursor 0); #2 GPT 'Gate-01 test post from GPT' (cursor 1); #3 Claude 'Gate-01 reverse delivery confirmed by Claude' (cursor 2).
- Reported recovery: Claude context [1,2,3], unseen []; GPT context [1,2], unseen [3]. Uvicorn restart and tunnel hostname change did not destroy the ledger. Ledger and backup reported three lines each; current bytes UNKNOWN.
- Frozen source commit reported: b539bd8ef2282cedf0b57c2d1d84c50b6fecd941 in Stratumnova/pockettest. Original JSONL is on phone, not necessarily in GitHub. Do not reuse exposed secret paths.

## Gate-02 network — October 8–9
- Namecheap domain rodsrcpark.com delegated to Cloudflare; named tunnel pocket-server-gate02 and hostname roundtable.rodsrcpark.com. Initially HTTP 502 while origin absent, subsequently reported HTTP 200 /health after switching to Gate-02 port 8766.
- Public Gate-02A deployed **deny-all** at f0a11d5; /mcp 401, /register 404, /health {status: gate02a-deny-all, ready:false}. A healthy tunnel is not proof of authorized application access.
- Named-tunnel token was exposed in process output/chat; October 10 checkpoint reports rotation and 0600 token-file storage. Recheck credential state before any real activation; do not publish tokens.

## Gate-02A auth development — October 9–11
- Separate worktree ~/pockettest-c1 on build/gate02a-c1-auth-store; live ~/pockettest main stayed deny-all. Dev port 8767, public 8766.
- C1 SQLite auth store and admin CLI GREEN; C2 SDK dynamic registration with restricted Claude/ChatGPT callback patterns GREEN; C3 consent/PKCE and authorization-code lifecycle GREEN in the October 10 checkpoint, 110 tests reported at 1b578ee32532f99093ab906af52e8b485c90a7e4.
- Recorded parameters: 25-minute pending approval window, 9-minute code lifetime, 5 global pending requests, canonical MCP resource audience, single-use codes with concurrency/rollback tests.
- October 10 checkpoint: C3 browser consent-completion redirect still NEXT; C4 access/refresh tokens and C5 audit/scopes NOT STARTED. October 11 records still identify unfinished auth integration. **Empty token tables are not implemented token issuance.**
- Design distinguishes Gate-02A authentication, Gate-02B authenticated Roundtable, Gate-02C project files/vault; none should be treated as live solely because Gate-02 networking works.
- Review failures recorded: callback regex matched no legitimate ChatGPT URL, schema/migration issues, SDK-shape errors, reported changes absent from some commits. Targeted positive tests and commit-pinned source reviews are necessary.

## Later work and present successor — October 2026
- Subsequent A25 records discuss Shared Space Stage 1 (six-file checkpoint, 45 tests reported), terminal tools and October 19 Claude-side successful terminal interaction reports. These are **distinct implementations / historical claims** and do not prove the Gate-02A OAuth sequence was finished.
- A25 Systems Hub is the **official successor project**, with Pocket Server/Termux designated a historical temporary scaffold (Workstation Roundtable 01). Owner cutoff: October 19, 2026, 8:07 PM MDT (October 20, 02:07 UTC). Earlier work is REFERENCE, not automatically ADOPTED.
- New project's first milestone is Message Hub, then independently authenticated identities, scoped terminal tooling, backups, recovery, and owner-approved migration. Do not retire old infrastructure until independently verified and approved.
- Canonical project history belongs under A25-node1125_hub/A25.archives/projects/a25-systems-hub/; this Office inbox record is an intake/handoff, not a duplicate canonical project home.

## UNKNOWN / follow-up read-only checks
1. Confirm frozen Gate-01 source commit, three-event ledger and backup bytes, and preservation after subsequent phone changes.
2. Inspect current Gate-02 branch/main history for C3 completion, C4, C5, merge, and any actual live OAuth client tests A6–A9.
3. Establish current public server/terminal tool auth boundaries separately; verify no inherited secret-path trust.
4. Map Shared Space and terminal code to commits, owner approvals, test evidence, and present deployment; do not infer status from reports.
5. Index remaining ChatGPT export segments and reconcile original user requests/responses with these checkpoints.

## Source pointers
- Historical source PDFs in ChatGPT project uploads: 'Pocket_Server_Roundtable_Gate02_Checkpoint_2026-10-08(2).pdf'; 'Pocket_Server_Checkpoint_2.1_Gate02A_2026-10-09.pdf'; 'Pocket_Server_Checkpoint_3_C1-C3_2026-10-10.pdf'. These are cited by title because no public immutable URLs for their uploaded bytes were established.
- Historical source repository: https://github.com/Stratumnova/pockettest
- A25 Archives team charter: https://github.com/Stratumnova/A25-workspace.hub/blob/main/A25-node1125_hub/A25.office/teams/archives/README.md
- A25 Systems Hub original setup request: https://github.com/Stratumnova/A25-workspace.hub/blob/main/A25-node1125_hub/A25.office/teams/archives/requests/incoming/A25-SYSTEMS-HUB-AG-WR-20261020T020916Z.md
- Canonical project: https://github.com/Stratumnova/A25-workspace.hub/tree/main/A25-node1125_hub/A25.archives/projects/a25-systems-hub

**Archives action requested:** Review and index this historical note against original evidence; do not silently promote historical checkpoint assertions to VERIFIED or ADOPTED. No other action authorized.
