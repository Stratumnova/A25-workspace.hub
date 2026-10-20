"""Test-only single-owner command service composition; no listener or deployment.

All requests to this object share one dispatcher. Credentials are checked by
trusted callbacks, not caller-supplied flags. An exclusive mkdir marker prevents
cooperating second service instances on the tested filesystem. A stale marker
always denies startup; there is no automatic cleanup or takeover.

This is not a network service or production security boundary. A trusted ingress
must exclusively route all commands here, protect credential transport, and
prevent bypassing this service before deployment.
"""
from a25_directory_owner import DirectoryOwner
from a25_persistent_dispatcher import PersistentDispatcher


class SingleOwnerService:
    def __init__(self, verify_caller, verify_owner, *, marker=None, state_path=None):
        if not callable(verify_caller) or not callable(verify_owner):
            raise TypeError("STOP: trusted verifier callbacks required")
        self._owner = DirectoryOwner(marker)
        try:
            self._dispatcher = PersistentDispatcher(
                verify_caller, verify_owner, state_path=state_path
            )
        except BaseException:
            # Preserve marker on failure: restart needs manual review.
            raise

    def status(self):
        return self._dispatcher.status()

    def run(self, caller, credential, argv):
        return self._dispatcher.run(caller, credential, argv)

    def unlock(self, owner_credential):
        return self._dispatcher.unlock(owner_credential)

    def lock(self):
        return self._dispatcher.lock()

    def close(self):
        # No silent removal of ownership marker. Keep locked before release.
        result = self.lock()
        self._owner.release()
        return result
