# A25terminal — Owner Directive: Lock Incoming Remote Commands, Not Local Files

**Date:** 2026-10-20
**Authority:** Direct owner instruction (Zed)
**Status:** ADOPTED project requirement. Do not reinterpret as a filesystem-security project.

## Exact intent

The owner wants a manually controlled emergency lock on **incoming remote command and terminal-input paths through A25 tunnels and bridges**. This is an ingress-control requirement.

**DO NOT** make locking Downloads, Documents, Termux private storage, other local files, or ordinary local phone use the objective. The owner explicitly corrected this misunderstanding: “I told you we needed to lock the tunnels not the files. Incoming stuff not local.”

The previous assistant spent approximately three hours pursuing filesystem locking, single-owner filesystem markers, and Unix socket capabilities. Those tests may remain historical technical references, but **they are not evidence that the owner's actual request was implemented**. Do not continue that line of work without a concrete necessity to the incoming-command lock and explicit owner approval.

## Required behavior

1. **LOCK:** Stop/reject new remote commands and terminal input entering through every protected A25 tunnel/bridge command route. No command should bypass the ingress gate through an alternate A25 endpoint.
2. **Active remote commands:** Stop A25-managed commands already running when the lock is engaged; verify termination and report any survivors. Do not kill unrelated local Termux processes.
3. **UNLOCK:** Only the owner can manually unlock with a protected password/credential. No timer, automatic unlock, or secrets in chat, logs, command-line arguments, or GitHub.
4. **Caller authentication:** Even while unlocked, each remote caller must authenticate independently. Unknown callers are denied.
5. **Local access:** Ordinary local phone use, local Termux work, and access to Downloads/Documents must remain unaffected.
6. **Restart:** Fail closed for incoming remote command access following bridge/gateway restart or crash.
7. **Scope:** Inspect existing tunnel/bridge command entry points and enumerate bypass paths BEFORE proposing edits. No deployment, tunnel shutdown, service replacement, phone mutations outside previously authorized test boundary, or modification of existing bridges without a separate explicit approval.

## Next justified action

Perform a **READ-ONLY inventory** of the existing A25 Cloudflare tunnel, bridge, and other remote command entry points. Identify exactly where incoming commands reach Termux and what component can deny requests before execution. Produce a minimal, reversible ingress-lock design and obtain owner approval before changing live components.

## Evidence discipline

- **ADOPTED:** The owner requires locking **incoming** remote tunnel/bridge command paths, not local files.
- **HISTORICAL / REFERENCE:** Earlier file-lock, directory-owner, dispatcher, and socket experiments. They are not a deployed solution.
- **UNKNOWN:** Actual full inventory of live ingress routes and whether any bypass remains.
- **NOT VERIFIED:** Any claim that the owner's terminal is already protected by a master remote-command lock.

## Assistant handoff warning

**Do not repeat the three-hour scope drift.** Before any further engineering action, ask: “Does this directly prevent incoming remote commands through the A25 tunnel/bridge while leaving local files and local use alone?” If not, stop and return to the ingress requirement.
