"""A25 inbound bridge command admission gate (source-only; NOT deployed).

Integrate this into the ONE running MCP bridge before ANY tmux send-keys.
This protects remote input, not local filesystem operations. The bridge must
route every command-capable tool through the same gate, and restart locked.
"""
import threading


class InboundCommandGate:
    def __init__(self, verify_owner, verify_caller):
        if not callable(verify_owner) or not callable(verify_caller):
            raise TypeError("trusted owner and caller verifiers required")
        self._verify_owner = verify_owner
        self._verify_caller = verify_caller
        self._guard = threading.RLock()
        self._locked = True
        self._inflight = 0

    def status(self):
        with self._guard:
            return {"locked": self._locked, "inflight": self._inflight}

    def lock(self):
        """Stop accepting new remote terminal input; never affect local input."""
        with self._guard:
            self._locked = True
            return self.status()

    def unlock(self, owner_credential):
        if not self._verify_owner(owner_credential):
            raise PermissionError("STOP: owner authentication failed")
        with self._guard:
            self._locked = False
            return self.status()

    def send(self, caller, caller_credential, session, command, send_keys):
        """Authorize then deliver BOTH tmux writes under one admission lock.

        send_keys is a trusted bridge callback that executes the existing
        literal-input send-keys and Enter sequence. Never accept a remote
        callback, trusted flag, or authentication verdict from a caller.
        """
        if not isinstance(session, str) or not session:
            raise ValueError("STOP: invalid session")
        if not isinstance(command, str) or not command:
            raise ValueError("STOP: invalid command")
        if not self._verify_caller(caller, caller_credential):
            raise PermissionError("STOP: caller authentication failed")
        with self._guard:
            if self._locked:
                raise PermissionError("STOP: inbound terminal lock engaged")
            self._inflight += 1
            try:
                # Hold lock through both tmux writes: lock cannot interleave
                # between literal input and Enter.
                return send_keys(session, command)
            finally:
                self._inflight -= 1
