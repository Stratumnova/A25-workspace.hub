# A25 Termux — workshop Team Capability Notes

**Owner:** Zed
**Prepared by:** A25 GPT, read-only inspection and official documentation review
**Status:** Mixed VERIFIED local observations, documented general capabilities and UNKNOWN untested operations
**Scope:** Public-safe training notes; not a security audit or build order

## Team-specific findings

Verified device capability snapshot: Android 14/aarch64, Termux 0.118.3 F-Droid, Python 3.14.6, 116 installed packages, 15 available upgrades at inspection. Git, pip, SSH, curl, Cloudflared, tmux, Termux backup/restore and wake-lock helpers present. Node/npm, jq and sqlite3 CLI not found on PATH. Rolling-release upgrades require scheduled maintenance, backups and environment regression tests. Avoid updating Python during active test stages.

## Evidence and limitations

Local observations obtained through the authorized A25 GPT Terminal with read-only shell diagnostics, without changing packages, services, files or tunnels. The terminal's existing screen separately indicated F-Droid Termux 0.118.3 and no Termux:API. Package availability reflects the inspection moment only. No external endpoint or authentication audit was completed. Claude's earlier report is REFERENCE; matching observations were freshly checked, not adopted blindly.

Official documentation:
- [Termux execution environment](https://github.com/termux/termux-packages/wiki/Termux-execution-environment)
- [Termux filesystem layout](https://github.com/termux/termux-packages/wiki/Termux-file-system-layout)
- [Termux package management](https://github.com/termux/termux-packages/wiki/Package-Management)
- [Termux:API](https://github.com/termux/termux-api/blob/master/README.md)

**Boundary:** This note records capabilities and recommendations, not approval to upgrade, deploy, expose services, alter phone settings or share protected data. Do not place sensitive endpoint details or exploit information in public GitHub.
