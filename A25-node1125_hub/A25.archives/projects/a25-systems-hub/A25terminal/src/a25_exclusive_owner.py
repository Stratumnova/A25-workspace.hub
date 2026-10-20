"""Experimental exclusive dispatcher ownership; Android test folder only.

Uses nonblocking advisory flock. This protects cooperating processes only.
A process with direct shell access can bypass it; ingress still must be secured.
Do not use as a production security boundary without filesystem and crash tests.
"""
import fcntl
import os
from pathlib import Path

ROOT = Path("/storage/emulated/0/Documents/AI_Workshop/terminal tools test folder")
STORE = ROOT / "__a25terminal_control_v1__"


class ExclusiveOwner:
    def __init__(self, lock_path=None):
        self.path = Path(lock_path) if lock_path is not None else STORE / ".a25-owner-test.lock"
        self.fd = None
        if not ROOT.is_dir() or ROOT.is_symlink() or ROOT.resolve(strict=True) != ROOT:
            raise RuntimeError("STOP: test root unavailable")
        if not STORE.is_dir() or STORE.is_symlink() or STORE.resolve(strict=True) != STORE:
            raise RuntimeError("STOP: test store unavailable")
        if self.path.parent.resolve(strict=True) != STORE or self.path.is_symlink():
            raise RuntimeError("STOP: owner lock path redirected")
        flags = os.O_RDWR | os.O_CREAT | getattr(os, "O_CLOEXEC", 0) | getattr(os, "O_NOFOLLOW", 0)
        fd = os.open(self.path, flags, 0o600)
        try:
            fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except (OSError, BlockingIOError) as exc:
            os.close(fd)
            raise RuntimeError("STOP: dispatcher owner already active or lock unavailable") from exc
        self.fd = fd

    def close(self):
        if self.fd is not None:
            fd, self.fd = self.fd, None
            fcntl.flock(fd, fcntl.LOCK_UN)
            os.close(fd)

    def __enter__(self):
        return self

    def __exit__(self, *_):
        self.close()
