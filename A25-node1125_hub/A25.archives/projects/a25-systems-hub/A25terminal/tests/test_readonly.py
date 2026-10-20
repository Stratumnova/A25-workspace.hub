"""Unit tests use temporary disposable files only; never touch live A25 data."""
import contextlib
import io
import json
from pathlib import Path
from tempfile import TemporaryDirectory
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from a25_terminal_readonly import entries, main

class ReadOnlyTests(unittest.TestCase):
    def test_tree_and_find(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "example.txt").write_text("sample")
            (root / "folder").mkdir()
            self.assertEqual({x["path"] for x in entries(root)}, {"example.txt", "folder"})
            self.assertEqual([x["path"] for x in entries(root, "EXAMPLE")], ["example.txt"])

    def test_status_json(self):
        with contextlib.redirect_stdout(io.StringIO()) as output:
            code = main(["status"])
        self.assertEqual(code, 0)
        self.assertEqual(json.loads(output.getvalue())["action"], "status")

    def test_invalid_root(self):
        with contextlib.redirect_stderr(io.StringIO()):
            self.assertEqual(main(["tree", "--root", "/path-that-does-not-exist-a25"]), 1)

    def test_find_requires_term(self):
        with contextlib.redirect_stderr(io.StringIO()):
            with self.assertRaises(SystemExit):
                main(["find"])

if __name__ == "__main__":
    unittest.main()
