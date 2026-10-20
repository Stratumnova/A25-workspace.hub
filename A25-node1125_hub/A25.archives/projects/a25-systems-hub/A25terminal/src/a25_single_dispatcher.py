"""A25 experimental single-owner dispatcher. Not installed as a service.

The owner process must be the ONLY entry point for callers. This module does
not create a socket, authenticate network clients, or block legacy bridges.
Credentials are verified by a caller-supplied trusted verifier, not caller
assertions. A separate production ingress and persistence design is required.
"""
from a25_command_supervisor import CommandSupervisor


class SingleDispatcher:
    def __init__(self, verify_caller, verify_owner):
        if not callable(verify_caller) or not callable(verify_owner):
            raise TypeError("trusted verification callbacks required")
        self._verify_caller = verify_caller
        self._verify_owner = verify_owner
        self._supervisor = CommandSupervisor()

    def status(self):
        return self._supervisor.status()

    def run(self, caller_id, credential, argv):
        # Never accept an unauthenticated boolean supplied by a remote caller.
        if not self._verify_caller(caller_id, credential):
            raise PermissionError("STOP: caller authentication failed")
        return self._supervisor.dispatch(argv, authorized=True)

    def unlock(self, owner_credential):
        if not self._verify_owner(owner_credential):
            raise PermissionError("STOP: owner authentication failed")
        self._supervisor.unlock(owner_verified=True)
        return self.status()

    def lock(self):
        # No password is needed to lock; all active managed work is stopped.
        return self._supervisor.lock()
