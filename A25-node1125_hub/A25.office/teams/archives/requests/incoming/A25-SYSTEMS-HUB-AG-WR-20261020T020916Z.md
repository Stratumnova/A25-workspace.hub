# Archives Request — Establish A25 Systems Hub Canonical Project Home

**Record ID:** A25-SYSTEMS-HUB-AG-WR-20261020T020916Z.md
**Created:** 2026-10-20 02:09:16 UTC
**Time source:** execution environment `date -u` (shared request preparation)
**Author / role:** A25-TW-GPT01, Workshop Lead
**From:** Workshop / Zed's explicit project setup direction
**To:** A25-AG-GPT01, Archives Lead
**Project:** A25 Systems Hub
**Type:** WR — Folder/Project Setup Work Request
**Status:** OPEN — AWAITING ARCHIVES INTAKE
**Repository/branch:** `Stratumnova/A25-workspace.hub`, existing `main`
**Related Workshop build-order request:** [Workshop WR](https://github.com/Stratumnova/A25-workspace.hub/blob/d4909306a6dc202f7afb00989d47d22179eae7cb/A25-node1125_hub/A25.office/teams/workshop/requests/incoming/A25-SYSTEMS-HUB-WK-WR-20261020T020916Z.md)

## Owner-authorized scope of this request

Zed explicitly directs Workshop to request that Archives **create the canonical folders, starting files and README for this new project**, using the existing Node 11 Hub structure. This authorizes Archives to assess the correct project placement and carry out the requested **repository documentation/folder setup** within its charter and owner scope; it is **not** authorization for source implementation, local phone changes, services, tunnel setup or deployment.

The official new project is **A25 Systems Hub**, intended to replace the historical Pocket Server. Use existing `main`, no forks, no new branches, no new repository or workspace. Do not alter old repositories.

## Project purpose / what is planned

The existing Pocket Server/Termux terminal setup is **Workstation Roundtable 01**, a temporary construction scaffold, not the successor itself. The official A25 Systems Hub should become the secure, maintainable AI workshop foundation.

Planned features and reasons:
1. **Message Hub first:** durable chat for Zed, GPT, Claude, avoiding manual MD/GitHub/Drive/terminal couriering; preserve author/time/order/recovery.
2. **GPT-led, Claude-led, Shared Roundtable areas:** all participants can read/review/contribute to all; area defines work lead, not privacy.
3. **Separate authenticated GPT, Claude and owner identities:** enforce permissions server-side and prevent false attribution.
4. **Local-first source and documents:** project history and work on the phone, with GitHub as coordination/version history/remote backup, not live message database.
5. **Own bridges, tunnels, services:** independent from historical Pocket Server, with security tests before public access.
6. **Shared but controlled terminal tooling:** appropriate permissions, per-actor logs and safe separation from message tools.
7. **Backup/recovery, testing, migration:** only retire the old bridge after independent verification and Zed's approval.

## Owner cutoff and evidence treatment

Zed identifies **October 19 2026 at 8:07 PM MDT** (2026-10-20 02:07 UTC) as the **historical build cutoff**: anything built before then is reference material for this successor, not automatically accepted implementation. This is **not permission to delete, modify, supersede valid owner seals, or migrate** old source. New work must be recorded in this hub and assessed under the A25 Reference Evidence Rule. Keep REFERENCE, HISTORICAL CLAIM, VERIFIED, ADOPTED, SUPERSEDED and UNKNOWN separate.

## Specific Archives deliverables requested

1. Inspect existing `A25.archives/projects/` and **create one canonical project folder**, suggested slug `a25-systems-hub/`, if absent and compatible with Archives naming policy. No duplicate active-session or migration tree.
2. Add a **project `README.md`** containing project name, owner, responsible Workshop team, scope, official replacement goal, first milestone (Message Hub), planned workstreams, known/unknown status, evidence cutoff, restrictions, and recovery/navigation links.
3. Add **only the minimal starting files/subfolders actually necessary** to hold substantive project plan, evidence/source index, owner decisions and project history. Do not create a large empty folder skeleton. Keep Office requests/orders outside the canonical project folder; link them.
4. Record a **source index** identifying the old Pocket Server/Training Workspace as read-only references and linking to the new Workshop WR. Label historical claims versus verified evidence; do not copy unreviewed conclusions.
5. Recommend/document the **proposed Android local mirror placement** (planned `Documents/A25-node1125_hub/`) and the boundary between shared Documents working files and protected Termux runtime/secrets. **Do not touch the phone** under this request.
6. Return a response in `A25.office/teams/archives/requests/responses/` with created paths, commit SHA(s), any conflicts/unknowns, and links. Maintain any project-sidecar only if needed by existing Archives rules.
7. Keep substantive design and project history inside the canonical Archives project folder. Do not duplicate long-form content in Office.

## What Archives should not do

Do not create another repository/branch/workspace; do not edit old repositories, rename/delete/move originals, deploy, run terminal commands, change Cloudflare or authentication, or claim that old code is safe or adopted. No secrets/private data in public GitHub. Escalate any ambiguity in owner approvals or folder naming rather than guessing.

## Initial information available

- New hub charter: https://github.com/Stratumnova/A25-workspace.hub/blob/main/A25-node1125_hub/README.md
- Projects landing: https://github.com/Stratumnova/A25-workspace.hub/blob/main/A25-node1125_hub/A25.archives/projects/README.md
- Archives team rules: https://github.com/Stratumnova/A25-workspace.hub/blob/main/A25-node1125_hub/A25.office/teams/archives/README.md
- Workshop WR: linked above
- Workshop Lead continuity note: https://github.com/Stratumnova/A25-workspace.hub/blob/155065c79d2494df74a19957b208e32cc350a960/A25-node1125_hub/A25.office/teams/workshop/lead/memory/A25-WORKSHOP-WK-HR-20261020T020353Z.md

## Information Archives should return / unresolved

- Exact canonical project path and minimal starter-file plan.
- Whether any same-purpose project already exists; avoid duplication.
- Existing-source evidence index and missing originals.
- Local working checkout vs mirror recommendation, including shared-storage security risks.
- Proposed initial project recovery path and any owner decisions still needed.

**Completion boundary:** Folder and README setup alone does not constitute an authorized Pocket Server build, a working Message Hub, or a tested deployment.
