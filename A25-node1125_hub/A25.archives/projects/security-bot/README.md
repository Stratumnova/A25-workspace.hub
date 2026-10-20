# Security Bot — Active Project Landing

Owner: Zed
Responsible discipline: A25 Security Team
Project state: REQUIREMENTS CAPTURED; BUILD NOT ASSIGNED OR AUTHORIZED
Source status: historical Security Team investigation note; its conclusions are limited to its recorded inspection scope
Charter: [Node 11 Hub](../../README.md)

## Purpose
Future lightweight, evidence-backed security audit bot for answering **what changed, where, when, and how do we know?** across a defined monitored environment. The same folder is the working project home when authorized and its archive whenever inactive. No additional project home or mandatory archival migration is needed.

## Original source
- [A25-SEC-N003 — Terminal Input Audit and Future Security Bot Requirements](https://github.com/Stratumnova/A25-Training-Workspace/blob/6a34018f76ac5f4f22009de1b279ada4406ae711/project%20lead/leadership/security-team/team-lead/A25-SEC-N003-TERMINAL-INPUT-AUDIT-AND-FUTURE-SECURITY-BOT-2026-10-19.md) — original dated Security Team record; preserve in its source repository

## Requirements snapshot — REFERENCE / PROPOSED, NOT IMPLEMENTED
The original note proposes timestamped event records; distinctions between read/search, filesystem mutation, process/service changes and unknown activity; initial file hashes or manifests and change detection; read-only time-window queries; exact evidence pointers; coverage-gap reporting; redaction; and evaluation of existing Watchdog and Archives components before new implementation.

The key evidentiary distinction is **NO CHANGES OBSERVED IN COVERED SOURCES** versus **NO CHANGES VERIFIED**, which requires sufficiently complete monitoring coverage. The source did not prove that no changes occurred during the investigated period. Earlier historical inspection findings are not proof of present server state.

## Who handles what
- **Security:** owns requirements, audit interpretation and security review
- **Archives:** maintains this project home, provenance, recovery and original-source links
- **Training:** may design/evaluate lightweight bot components after authorization
- **Workshop:** owns any separately authorized terminal integration or live deployment
- **Audits:** may independently review evidence and coverage when assigned
- **Zed:** authorizes build scope, monitored paths, access, deployment and adoption

## Working and recovery rules
Start with the original A25-SEC-N003 and related records linked there, then the current Security Office and root charter. When authorized work begins, add actual designs, decisions, test evidence, implementation, failures and handoffs **here**, creating subfolders only when needed. The Office holds assignments and short links, not a duplicate project history.

Do not assume a builder has been assigned, monitoring exists, a baseline was collected, or any test passed. The note's suggested controlled tests are proposals, not permission to run them. Do not inspect unrelated personal files or alter phone, bridge, tunnel, credentials or Workshop runtime without explicit authorization. Do not store raw secrets or private command contents in public GitHub.

## Open questions
Exact monitored paths/exclusions, evidence retention and custody, trustworthy baseline method, permissions, resource budget, Watchdog/Archives reuse, test scope and deployment approval remain to be decided.
