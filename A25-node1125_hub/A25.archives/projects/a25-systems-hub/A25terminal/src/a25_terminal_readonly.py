"""A25 Terminal read-only inspection CLI (Phase 1 foundation).

No subprocess shell, writes, network calls, or service changes.
Run: python -m a25_terminal_readonly status|tree|find|processes|sessions|health
"""
import argparse
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys

def command(argv, timeout=8):
    try:
        result = subprocess.run(argv, text=True, capture_output=True, timeout=timeout, check=False)
        return {"returncode": result.returncode, "stdout": result.stdout[:16000], "stderr": result.stderr[:4000]}
    except (OSError, subprocess.TimeoutExpired) as exc:
        return {"returncode": None, "error": type(exc).__name__ + ": " + str(exc)}

def root_path(value):
    root = Path(value).expanduser().resolve(strict=True)
    if not root.is_dir():
        raise ValueError("Root must be an existing directory")
    return root

def entries(root, term=None, limit=200):
    found = []
    for current, dirs, files in os.walk(root, followlinks=False):
        dirs.sort()
        files.sort()
        for name in dirs + files:
            item = Path(current) / name
            if term is None or term.casefold() in name.casefold():
                found.append({"path": str(item.relative_to(root)), "kind": "directory" if item.is_dir() else "file"})
                if len(found) >= limit:
                    return found
    return found

def main(argv=None):
    parser = argparse.ArgumentParser(description="A25 read-only local diagnostics")
    parser.add_argument("action", choices=["status", "tree", "find", "processes", "sessions", "health"])
    parser.add_argument("--root", default=".")
    parser.add_argument("--term")
    parser.add_argument("--limit", type=int, default=200)
    args = parser.parse_args(argv)
    if not 1 <= args.limit <= 1000:
        parser.error("--limit must be between 1 and 1000")
    try:
        if args.action in ("tree", "find"):
            root = root_path(args.root)
            if args.action == "find" and not args.term:
                parser.error("find requires --term")
            result = {"root": str(root), "entries": entries(root, args.term if args.action == "find" else None, args.limit)}
        elif args.action == "status":
            result = {"cwd": os.getcwd(), "home": str(Path.home()), "python": sys.version.split()[0],
                      "commands": {name: shutil.which(name) is not None for name in
                                   ("tmux", "git", "python", "jq", "sqlite3", "rsync", "sv", "ps", "ss")}}
        elif args.action == "processes":
            result = command(["ps", "-ef"])
        elif args.action == "sessions":
            result = command(["tmux", "list-sessions"])
        else:
            result = {"processes": command(["ps", "-ef"]), "sessions": command(["tmux", "list-sessions"])}
        print(json.dumps({"action": args.action, "result": result}, indent=2))
        return 0
    except (OSError, ValueError) as exc:
        print(json.dumps({"action": args.action, "error": str(exc)}), file=sys.stderr)
        return 1

if __name__ == "__main__":
    raise SystemExit(main())
