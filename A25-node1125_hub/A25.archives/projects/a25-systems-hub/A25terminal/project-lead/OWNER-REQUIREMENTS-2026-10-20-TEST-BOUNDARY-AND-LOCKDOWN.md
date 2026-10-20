# A25terminal — Owner Requirements: Authorized Test Boundary and System Lockdown

**Owner and project lead:** Zed
**Date:** 2026-10-20 (conversation date; no independent clock claim)
**Status:** ADOPTED owner requirements for testing and design; lockdown implementation UNKNOWN
**Relationship:** Addendum to [Owner-Approved Build Plan V1](../APPROVED-BUILD-PLAN-V1.md); does not rewrite the approved historical record.
**Evidence basis:** Owner instructions in current ChatGPT project conversation, and direct read-only terminal inspection and controlled tests reported there.

## 1. Exact authorized test boundary

The owner authorizes all necessary **file-operation tests** for A25terminal controls inside this exact Android shared-storage directory, including its copied contents:

`/storage/emulated/0/Documents/AI_Workshop/terminal tools test folder`

This is an **exclusive path boundary**, not permission to modify neighboring files or directories. Before **every mutating operation**, verify that the root exists, is a directory, is not a symbolic link, and resolves to the **exact same absolute path**. Verify each intended target stays beneath that root after path resolution; reject symlink escapes, traversal, and unsafe archive members. If any verification fails, **disengage without mutation and report to Zed**. Do not treat parent `AI_Workshop/`, historical projects, running bridge/tunnel, or other storage as test targets.

The owner confirms these are copied, disposable materials. No separate `a25terminal-test-fixtures` folder elsewhere is authorized. Tests may create, edit, copy, rename, move, delete and unzip **inside this root only**, within their actual approved scope. Preserve original ZIPs when testing extraction so integrity can be compared. Do not infer permission to install packages, restart services, or change phone-wide settings from file-test authorization.

## 2. Build the new controls, then test those controls

The owner clarified that the project must **build and test the new A25terminal controls**, not merely demonstrate what the existing historical terminal connection can already do.

For each control: (1) implement and version its source in this component; (2) perform review and tests; (3) deploy only when separately authorized, in an isolated location that does not replace the working bridge; (4) invoke **the new control** against the approved test boundary; (5) record exact observed results and failures; (6) obtain acceptance before promoting it. Existing terminal capabilities are transport and REFERENCE evidence, not automatic certification of new code.

## 3. Owner-required password-controlled system lockdown

Zed requests a **lockdown mode** in which **no AI or human can perform operations without Zed's password**. Treat this as a design and security requirement for a **fail-closed, owner-controlled lock**, not as a claim that Android or physical access is already blocked.

Required design questions and controls:
- Define exactly which surfaces are controlled: GPT, Claude, future bots, local toolkit CLI, network gateway, interactive sessions, service lifecycle, existing terminals and any other routes to command execution.
- When locked, deny all non-recovery control operations at a common enforcement point, including reads if the owner intends *nothing* accessible; prohibit bypass by alternate authenticated principals or older interfaces.
- Unlock only after secure verification of an owner secret; never put the password, plaintext equivalents, reusable tokens or hashes in public GitHub, command logs, ChatGPT messages or shell history.
- Provide rate limiting, replay resistance, authenticated principal checks, durable lock state, audited lock/unlock attempts and fail-closed behavior across service restart or network loss.
- Prevent currently running commands and already-open sessions from bypassing lock; define whether lock suspends, terminates, or quarantines them, and preserve an independently accessible owner recovery procedure.
- Security must examine the distinction between **toolkit-wide lock** and **device-wide lock**. Ordinary Termux user-space software cannot guarantee exclusion of the device owner, Android OS, root/ADB users, other applications or physical-access actors. Any stronger device-wide guarantee needs separate feasibility review and owner approval.
- No default password, automatic unlock, autonomous execution or destructive lockdown experiment. Ask Zed to choose credential enrollment, recovery, lock scope and emergency behavior before implementation.

**Status:** Requirement ADOPTED; design and feasibility pending; implementation/test/deployment UNKNOWN. The existing approved V1 plan remains authoritative for its original scope, with this owner-requested addition separately tracked.

## 4. Observed test evidence (historical terminal transport, not new toolkit acceptance)

Read-only terminal checks verified the exact root and found 64 nested directories and 152 files before testing. Existing terminal transport successfully performed create/edit/copy/rename/move and a scoped delete. Initial standard ZIP extraction stopped with an Android shared-storage PermissionError on a special-character path; a later sanitized-name extraction completed 82 entries (57 files and 25 directories) with file-hash comparison. The owner also inspected an extracted folder through Android's file manager. These are **observations of the existing terminal connection**, not passing acceptance tests of the new A25terminal implementation.

The approved original build plan, its approval ticket, and historical original request are not modified by this addendum.

## 5. Next authorized work

Implement controls in the existing `A25terminal/` project and test **the controls themselves**. Maintain distinct implementation, verification, owner acceptance, Security review and deployment records. Before any device installation or live service modification, seek explicit scope. For lockdown, complete the threat model and obtain Security review and owner's decisions before enforcing it.
