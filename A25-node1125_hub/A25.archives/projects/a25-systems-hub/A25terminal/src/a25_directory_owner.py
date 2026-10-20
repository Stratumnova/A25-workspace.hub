"""Test-only fail-closed single-owner marker for Android shared storage.

A directory creation is attempted once. Existing marker always denies startup.
Never automatically remove or reclaim a marker; after a crash, manual review is
required. Not a security boundary against noncooperating callers/processes.
"""
import os
from pathlib import Path

ROOT = Path("/storage/emulated/0/Documents/AI_Workshop/terminal tools test folder")
STORE = ROOT / "__a25terminal_control_v1__"


class DirectoryOwner:
    def __init__(self, marker=None):
        self.marker = Path(marker) if marker is not None else STORE / ".a25-owner-test.marker"
        self.acquired = False
        if not ROOT.is_dir() or ROOT.is_symlink() or ROOT.resolve(strict=True) != ROOT:
            raise RuntimeError("STOP: invalid authorized root")
        if not STORE.is_dir() or STORE.is_symlink() or STORE.resolve(strict=True) != STORE:
            raise RuntimeError("STOP: invalid authorized store")
        if self.marker.parent.resolve(strict=True) != STORE or self.marker.is_symlink():
            raise RuntimeError("STOP: invalid marker path")
        try:
            os.mkdir(self.marker, 0o700)
        except FileExistsError as exc:
            raise RuntimeError("STOP: ownership marker exists; manual review required") from exc
        except OSError as exc:
            raise RuntimeError("STOP: ownership marker creation failed") from exc
        self.acquired = True

    def release(self):
        """Deliberately does not remove marker: prevent unsafe silent reclaim."""
        self.acquired = False
