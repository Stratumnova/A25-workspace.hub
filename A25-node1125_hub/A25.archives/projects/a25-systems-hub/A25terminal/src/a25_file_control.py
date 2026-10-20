"""A25 Terminal: bounded file controls, experimental V1.

All mutating actions are restricted to the owner's exact test directory.
No shell execution, service control, network calls, or password handling.
"""
import argparse
import hashlib
import json
from pathlib import Path
import shutil
import stat
import zipfile

ROOT = Path("/storage/emulated/0/Documents/AI_Workshop/terminal tools test folder")
BAD = set('<>:"\\|?*')

MAX_ZIP_ENTRIES = 1000
MAX_ZIP_TOTAL_BYTES = 64 * 1024 * 1024
MAX_ZIP_MEMBER_BYTES = 16 * 1024 * 1024

class BoundaryError(Exception):
    pass

def verify_root():
    if not ROOT.is_dir() or ROOT.is_symlink() or ROOT.resolve(strict=True) != ROOT:
        raise BoundaryError("STOP: authorized root missing or redirected")
    return ROOT

def target(relative, must_exist=False):
    root = verify_root()
    p = Path(relative)
    if p.is_absolute() or not p.parts or any(part in (".", "..") for part in p.parts):
        raise BoundaryError("STOP: invalid relative path")
    candidate = root.joinpath(*p.parts)
    resolved = candidate.resolve(strict=must_exist)
    if resolved == root or not resolved.is_relative_to(root):
        raise BoundaryError("STOP: target outside authorized root")
    if must_exist and not candidate.exists():
        raise BoundaryError("STOP: target missing")
    return candidate

def run(action, source=None, dest=None, text=None):
    verify_root()
    if action == "list":
        folder = target(source, True) if source else ROOT
        if not folder.is_dir():
            raise BoundaryError("STOP: not a directory")
        return {"entries": sorted(p.name for p in folder.iterdir())}
    if action == "read":
        return {"text": target(source, True).read_text(encoding="utf-8")}
    if action == "hash":
        return {"sha256": hashlib.sha256(target(source, True).read_bytes()).hexdigest()}
    if action == "create":
        p = target(source)
        with p.open("x", encoding="utf-8") as f:
            f.write(text or "")
        return {"created": source}
    if action == "edit":
        p = target(source, True)
        if not p.is_file():
            raise BoundaryError("STOP: edit requires file")
        p.write_text(text or "", encoding="utf-8")
        return {"edited": source}
    if action in ("copy", "move"):
        src = target(source, True)
        dst = target(dest)
        if dst.exists() or dst.is_symlink():
            raise BoundaryError("STOP: destination already exists")
        if not src.is_file() or src.is_symlink():
            raise BoundaryError("STOP: source must be ordinary file")
        if action == "copy":
            shutil.copyfile(src, dst)
        else:
            src.rename(dst)
        return {action: [source, dest]}
    if action == "delete":
        p = target(source, True)
        if not p.is_file() or p.is_symlink():
            raise BoundaryError("STOP: delete requires ordinary file")
        p.unlink()
        return {"deleted": source}
    if action == "unzip":
        src = target(source, True)
        dst = target(dest)
        if dst.exists() or dst.is_symlink() or not zipfile.is_zipfile(src):
            raise BoundaryError("STOP: invalid ZIP or existing destination")
        with zipfile.ZipFile(src) as z:
            mapping = []
            members = z.infolist()
            if len(members) > MAX_ZIP_ENTRIES or sum(m.file_size for m in members) > MAX_ZIP_TOTAL_BYTES or any(m.file_size > MAX_ZIP_MEMBER_BYTES for m in members):
                raise BoundaryError("STOP: ZIP exceeds resource limits")
            for member in members:
                if ((member.external_attr >> 16) & 0o170000) == stat.S_IFLNK:
                    raise BoundaryError("STOP: ZIP symlink")
                parts = member.filename.rstrip("/").split("/")
                if not parts or any(x in ("", ".", "..") for x in parts) or member.filename.startswith("/"):
                    raise BoundaryError("STOP: ZIP traversal")
                cleaned = ["".join("_" if c in BAD or ord(c) < 32 else c for c in part) for part in parts]
                out = dst.joinpath(*cleaned)
                if not out.resolve().is_relative_to(dst):
                    raise BoundaryError("STOP: ZIP escape")
                mapping.append((member, out))
            if len(set(str(out) for _, out in mapping)) != len(mapping):
                raise BoundaryError("STOP: ZIP sanitized name collision")
            dst.mkdir()
            count = 0
            for member, out in mapping:
                verify_root()
                if member.is_dir():
                    out.mkdir(parents=True, exist_ok=True)
                else:
                    out.parent.mkdir(parents=True, exist_ok=True)
                    with z.open(member) as f, out.open("xb") as g:
                        remaining = member.file_size
                        while remaining:
                            chunk = f.read(min(1024 * 1024, remaining))
                            if not chunk:
                                raise IOError("ZIP member truncated")
                            g.write(chunk)
                            remaining -= len(chunk)
                        if f.read(1):
                            raise BoundaryError("STOP: ZIP member exceeds declared size")
                    with z.open(member) as f:
                        expected = hashlib.sha256(f.read()).digest()
                    if hashlib.sha256(out.read_bytes()).digest() != expected:
                        raise IOError("ZIP content mismatch")
                    count += 1
            return {"archive_entries": len(mapping), "verified_files": count, "destination": dest}
    raise ValueError("Unknown action")

def main(argv=None):
    parser = argparse.ArgumentParser(description="A25 bounded file control")
    parser.add_argument("action", choices=["list","read","hash","create","edit","copy","move","delete","unzip"])
    parser.add_argument("--source")
    parser.add_argument("--dest")
    parser.add_argument("--text")
    args = parser.parse_args(argv)
    try:
        print(json.dumps({"action": args.action, "result": run(args.action,args.source,args.dest,args.text)}, ensure_ascii=False))
        return 0
    except (BoundaryError, OSError, ValueError, zipfile.BadZipFile) as exc:
        print(json.dumps({"action": args.action, "error": str(exc)}, ensure_ascii=False))
        return 1

if __name__ == "__main__":
    raise SystemExit(main())
