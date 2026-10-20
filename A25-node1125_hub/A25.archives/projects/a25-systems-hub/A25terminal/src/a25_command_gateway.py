"""A25 master-lock gateway prototype (test only; not connected to legacy bridges).

All operations remain bounded by the owner's authorized test folder.
This is not a production multi-client command gateway.
"""
import argparse
import getpass
import hashlib
import hmac
import json
import os
from pathlib import Path
import secrets
import subprocess
import sys

ROOT = Path("/storage/emulated/0/Documents/AI_Workshop/terminal tools test folder")
STORE = ROOT / "__a25terminal_control_v1__"
STATE = STORE / ".gateway-lock.json"
CREDENTIAL = STORE / ".gateway-credential.json"
CONTROL = STORE / "a25_file_control_atomic.py"
ALLOWED = {"list", "read", "hash", "create", "edit", "copy", "move", "delete", "unzip"}

def verify():
    if not ROOT.is_dir() or ROOT.is_symlink() or ROOT.resolve(strict=True) != ROOT:
        raise RuntimeError("STOP: authorized test root unavailable")
    if not STORE.is_dir() or STORE.is_symlink() or not STORE.resolve(strict=True).is_relative_to(ROOT):
        raise RuntimeError("STOP: gateway test directory unavailable")
    for path in (STATE, CREDENTIAL, CONTROL):
        if path.is_symlink() or not path.resolve().is_relative_to(ROOT):
            raise RuntimeError("STOP: gateway path redirected")

def atomic_json(path, payload):
    verify()
    tmp = STORE / (".gateway-" + secrets.token_hex(12) + ".tmp")
    try:
        with tmp.open("x", encoding="utf-8") as f:
            os.chmod(tmp, 0o600)
            json.dump(payload, f)
            f.flush()
            os.fsync(f.fileno())
        os.replace(tmp, path)
    finally:
        tmp.unlink(missing_ok=True)

def state():
    verify()
    try:
        value = json.loads(STATE.read_text())
    except (OSError, ValueError):
        return True
    return value.get("version") != 1 or value.get("locked") is not False

def enroll():
    if CREDENTIAL.exists() or STATE.exists():
        raise RuntimeError("STOP: already enrolled")
    password = getpass.getpass("Set disposable TEST password: ")
    confirm = getpass.getpass("Repeat TEST password: ")
    if len(password) < 12 or password != confirm:
        raise RuntimeError("STOP: invalid test password")
    salt = secrets.token_bytes(16)
    digest = hashlib.scrypt(password.encode(), salt=salt, n=16384, r=8, p=1)
    atomic_json(CREDENTIAL, {"salt": salt.hex(), "digest": digest.hex()})
    atomic_json(STATE, {"version": 1, "locked": True})
    print(json.dumps({"enrolled": True, "locked": True}))

def unlock():
    if not CREDENTIAL.is_file():
        raise RuntimeError("STOP: no test credential enrolled")
    record = json.loads(CREDENTIAL.read_text())
    password = getpass.getpass("TEST password: ")
    actual = hashlib.scrypt(password.encode(), salt=bytes.fromhex(record["salt"]), n=16384, r=8, p=1)
    if not hmac.compare_digest(actual, bytes.fromhex(record["digest"])):
        raise RuntimeError("STOP: incorrect password")
    atomic_json(STATE, {"version": 1, "locked": False})
    print(json.dumps({"unlocked": True}))

def run(arguments):
    if state():
        raise RuntimeError("STOP: master command lock engaged")
    if not arguments or arguments[0] not in ALLOWED:
        raise RuntimeError("STOP: invalid action")
    if not CONTROL.is_file() or CONTROL.is_symlink():
        raise RuntimeError("STOP: control unavailable")
    return subprocess.call([sys.executable, str(CONTROL), *arguments])

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("action", choices=("enroll", "status", "lock", "unlock", "run"))
    parser.add_argument("arguments", nargs=argparse.REMAINDER)
    args = parser.parse_args()
    verify()
    if args.action == "enroll":
        enroll()
    elif args.action == "status":
        print(json.dumps({"locked": state(), "scope": "prototype gateway only", "legacy_bridges_blocked": False}))
    elif args.action == "lock":
        atomic_json(STATE, {"version": 1, "locked": True})
        print(json.dumps({"locked": True, "active_command_cancellation": "NOT IMPLEMENTED"}))
    elif args.action == "unlock":
        unlock()
    else:
        sys.exit(run(args.arguments))

if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(json.dumps({"error": str(exc)}))
        sys.exit(1)
