"""Isolated tests for a25_inbound_gate; no tmux, tunnel or phone effects."""
import unittest
from a25_inbound_gate import InboundCommandGate


class GateTests(unittest.TestCase):
    def setUp(self):
        self.events = []
        self.gate = InboundCommandGate(lambda p: p == "disposable-owner",
                                       lambda who, key: (who, key) == ("gpt", "disposable-caller"))

    def send(self, session, command):
        self.events.append((session, command))
        return "sent"

    def test_restart_defaults_locked(self):
        self.assertTrue(self.gate.status()["locked"])
        with self.assertRaises(PermissionError):
            self.gate.send("gpt", "disposable-caller", "a25-gpt", "echo ok", self.send)
        self.assertEqual(self.events, [])

    def test_bad_owner_cannot_unlock(self):
        with self.assertRaises(PermissionError):
            self.gate.unlock("bad")
        self.assertTrue(self.gate.status()["locked"])

    def test_good_owner_and_caller(self):
        self.gate.unlock("disposable-owner")
        self.assertEqual(self.gate.send("gpt", "disposable-caller", "a25-gpt", "echo ok", self.send), "sent")
        self.assertEqual(self.events, [("a25-gpt", "echo ok")])

    def test_unknown_caller_denied_when_unlocked(self):
        self.gate.unlock("disposable-owner")
        with self.assertRaises(PermissionError):
            self.gate.send("unknown", "bad", "a25-gpt", "echo no", self.send)
        self.assertEqual(self.events, [])

    def test_relock_blocks(self):
        self.gate.unlock("disposable-owner")
        self.gate.lock()
        with self.assertRaises(PermissionError):
            self.gate.send("gpt", "disposable-caller", "a25-gpt", "echo no", self.send)
        self.assertEqual(self.events, [])

    def test_callback_failure_resets_inflight(self):
        self.gate.unlock("disposable-owner")
        def broken(*args):
            raise RuntimeError("send failed")
        with self.assertRaises(RuntimeError):
            self.gate.send("gpt", "disposable-caller", "a25-gpt", "echo ok", broken)
        self.assertEqual(self.gate.status()["inflight"], 0)


if __name__ == "__main__":
    unittest.main()
