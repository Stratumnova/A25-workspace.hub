# A25terminal — Hardened ZIP Live Retest

**Status:** VERIFIED for specified test cases; broader Security acceptance UNKNOWN
**Owner:** Zed
**Date:** 2026-10-20
**Source revision:** `8400a22d24a7dd8ab2fc6a0161c4c8e674ef2d40`
**Downloaded source SHA-256:** `8f15e9f742a4f195991105358a2e11e0a959a113bf359bf75b30ab40449f7f6f`

## Exact authorized scope
All test writes were confined to `/storage/emulated/0/Documents/AI_Workshop/terminal tools test folder/__a25terminal_control_v1__/`. The root was checked for existence, directory type, no symlink, and exact resolved path before testing. The existing terminal transport carried commands; the new `a25_file_control_hardened.py` handled file operations.

## Live results
1. **PASS:** Retrieved exact GitHub revision by commit and installed the 6,469-byte source under the authorized test root.
2. **PASS:** `hash` returned `3880113d1e835a0770c2d2a4cae9b7bd36e5817ade70bafe94ae55d919f26b6b` for the original test file.
3. **PASS:** `unzip` on `Stratumnova-vault-main (4)_test08.zip` reported 82 archive entries and 57 hash-verified files in `__a25terminal_control_v1__/extracted_hardened`.
4. **PASS:** `read --source ../forbidden` was rejected with `STOP: invalid relative path`.
5. **PASS:** A ZIP created **inside the authorized test folder** containing one 16 MiB + 1 byte uncompressed member was rejected with exit code 1, `STOP: ZIP exceeds resource limits`, and **no extraction destination created**. Compressed archive size was 16,433 bytes.

## Limits and caveats
The negative test confirms the **per-member declared-size ceiling** in this scenario. It does not independently test 1,000-entry or 64 MiB aggregate ceilings, forged ZIP metadata, concurrency, races, interruption recovery, password lock, or adversarial bypass. No existing bridge or tunnel was modified. This is functional verification, not production certification.

## Next work
Add further boundary/negative tests, atomic write strategy, and owner-requested manual command-lock design with secure password entry. Security review required before claiming comprehensive enforcement.
