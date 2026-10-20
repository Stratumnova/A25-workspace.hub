"""Experimental in-process A25 command supervisor.

This module is NOT a command gateway, listener, or production service.
A future single gateway service must own one instance and authenticate
requests before calling dispatch(). It must never be instantiated separately
for each client, because separate instances would not share lock state.
"""
import os
import signal
import subprocess
import threading


class CommandSupervisor:
    def __init__(self):
        self._guard = threading.RLock()
        self._locked = True
        self._active = set()

    def status(self):
        with self._guard:
            return {"locked": self._locked,
                    "active": sum(p.poll() is None for p in self._active)}

    def dispatch(self, argv, *, authorized=False):
        """Run an already validated argv; refuse unauthenticated requests."""
        with self._guard:
            if not authorized:
                raise PermissionError("STOP: caller authorization required")
            if self._locked:
                raise PermissionError("STOP: master command lock engaged")
            if not isinstance(argv, (list, tuple)) or not argv or not all(
                isinstance(x, str) and x for x in argv
            ):
                raise ValueError("STOP: invalid command arguments")
            proc = subprocess.Popen(argv, start_new_session=True)
            self._active.add(proc)
        try:
            return proc.wait()
        finally:
            with self._guard:
                self._active.discard(proc)

    def unlock(self, *, owner_verified=False):
        with self._guard:
            if not owner_verified:
                raise PermissionError("STOP: owner verification required")
            self._locked = False

    def lock(self, *, terminate_timeout=2):
        """Deny new dispatch first, then stop all tracked process groups.

        Returns an explicit failure if any managed process survives.
        No unrelated process or legacy bridge is targeted.
        """
        with self._guard:
            self._locked = True
            failures = []
            for proc in tuple(self._active):
                if proc.poll() is None:
                    try:
                        os.killpg(proc.pid, signal.SIGTERM)
                        proc.wait(timeout=terminate_timeout)
                    except ProcessLookupError:
                        pass
                    except subprocess.TimeoutExpired:
                        try:
                            os.killpg(proc.pid, signal.SIGKILL)
                            proc.wait(timeout=terminate_timeout)
                        except ProcessLookupError:
                            pass
                        except subprocess.TimeoutExpired:
                            failures.append(proc.pid)
                if proc.poll() is None and proc.pid not in failures:
                    failures.append(proc.pid)
                if proc.poll() is not None:
                    self._active.discard(proc)
            return {"locked": not failures, "failed_to_stop": failures,
                    "new_dispatch_blocked": True}
