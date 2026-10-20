"""Test-only composition of authenticated dispatcher, supervisor and restart lock.

Not a network service. The trusted host must own ONE instance, verify credentials,
and prevent alternative command routes. No caller can supply verification booleans.
"""
import threading

from a25_command_supervisor import CommandSupervisor
from a25_persistent_lock import PersistentLock


class PersistentDispatcher:
    def __init__(self, verify_caller, verify_owner, state_path=None):
        if not callable(verify_caller) or not callable(verify_owner):
            raise TypeError("trusted credential verifiers required")
        self._guard = threading.RLock()
        self._verify_caller = verify_caller
        self._verify_owner = verify_owner
        self._lock_state = PersistentLock() if state_path is None else PersistentLock(state_path)
        self._supervisor = CommandSupervisor()  # starts locked

    def status(self):
        with self._guard:
            state = self._supervisor.status()
            # A persisted locked state must always override in-memory unlock.
            if self._lock_state.status()["locked"]:
                state["locked"] = True
            return state

    def run(self, caller, credential, argv):
        if not self._verify_caller(caller, credential):
            raise PermissionError("STOP: caller authentication failed")
        with self._guard:
            if self._lock_state.status()["locked"]:
                raise PermissionError("STOP: persistent master lock engaged")
        # Never hold dispatcher guard while waiting for a child. The supervisor
        # atomically rejects or registers dispatch against its own lock; a
        # simultaneous lock either wins first or cancels the registered child.
        return self._supervisor.dispatch(argv, authorized=True)

    def unlock(self, credential):
        if not self._verify_owner(credential):
            raise PermissionError("STOP: owner authentication failed")
        with self._guard:
            self._lock_state.unlock(owner_verified=True)
            try:
                self._supervisor.unlock(owner_verified=True)
            except Exception:
                self._lock_state.lock()
                raise
            return self.status()

    def lock(self):
        with self._guard:
            # Block new requests in this process before stopping tracked children.
            result = self._supervisor.lock()
            self._lock_state.lock()
            return result
