"""A25 test-only fail-closed persistent master lock.

One trusted process owns this object. This is NOT a cross-process lock,
network listener, credential verifier, or production security boundary.
State is confined to the owner-authorized Android test folder.
"""
import json
import os
from pathlib import Path
import secrets
import threading

ROOT = Path("/storage/emulated/0/Documents/AI_Workshop/terminal tools test folder")
STORE = ROOT / "__a25terminal_control_v1__"
STATE = STORE / ".a25-persistent-lock-test.json"


class PersistentLock:
    def __init__(self, state_path=STATE):
        self._guard = threading.RLock()
        self._state_path = Path(state_path)
        self._locked = True
        self._verify_path()
        # Conservative restart policy: never resume unlocked from disk.
        # Existing state is read only to detect malformed or unsafe paths.
        if self._state_path.exists():
            self._read_state()
        self._write_state(True)

    def _verify_path(self):
        if not ROOT.is_dir() or ROOT.is_symlink() or ROOT.resolve(strict=True) != ROOT:
            raise RuntimeError("STOP: test root unavailable")
        if not STORE.is_dir() or STORE.is_symlink() or not STORE.resolve(strict=True).is_relative_to(ROOT):
            raise RuntimeError("STOP: test store unavailable")
        if self._state_path.is_symlink() or self._state_path.parent.resolve(strict=True) != STORE.resolve(strict=True):
            raise RuntimeError("STOP: state path redirected")

    def _read_state(self):
        self._verify_path()
        try:
            data = json.loads(self._state_path.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            return True
        if not isinstance(data, dict) or data.get("version") != 1 or type(data.get("locked")) is not bool:
            return True
        return data["locked"]

    def _write_state(self, locked):
        self._verify_path()
        tmp = STORE / (".a25-lock-" + secrets.token_hex(12) + ".tmp")
        try:
            with tmp.open("x", encoding="utf-8") as f:
                os.chmod(tmp, 0o600)
                json.dump({"version": 1, "locked": locked}, f)
                f.flush()
                os.fsync(f.fileno())
            os.replace(tmp, self._state_path)
        finally:
            tmp.unlink(missing_ok=True)

    def status(self):
        with self._guard:
            return {"locked": self._locked}

    def unlock(self, *, owner_verified=False):
        with self._guard:
            if not owner_verified:
                raise PermissionError("STOP: owner verification required")
            self._write_state(False)
            self._locked = False

    def lock(self):
        with self._guard:
            self._locked = True
            self._write_state(True)
