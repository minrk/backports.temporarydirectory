"""Backport tempfile.TemporaryDirectory from Python 3.5.1

Copyright (C) PSF, Python Software License.
"""

# Imports.

import warnings as _warnings
import shutil as _shutil
import weakref as _weakref

from tempfile import mkdtemp

try:
    ResourceWarning
except NameError:
    ResourceWarning = RuntimeWarning # py2


__version__ = '3.5.1'


class TemporaryDirectory(object):
    """Create and return a temporary directory.  This has the same
    behavior as mkdtemp but can be used as a context manager.  For
    example:

        with TemporaryDirectory() as tmpdir:
            ...

    Upon exiting the context, the directory and everything contained
    in it are removed.
    """

    def __init__(self, suffix=None, prefix=None, dir=None):
        self.name = mkdtemp(suffix or '', prefix or '', dir or '')
        self._finalizer = _weakref.finalize(
            self, self._cleanup, self.name,
            warn_message="Implicitly cleaning up {!r}".format(self))

    @classmethod
    def _cleanup(cls, name, warn_message):
        _shutil.rmtree(name)
        _warnings.warn(warn_message, ResourceWarning)

    def __repr__(self):
        return "<{} {!r}>".format(self.__class__.__name__, self.name)

    def __enter__(self):
        return self.name

    def __exit__(self, exc, value, tb):
        self.cleanup()

    def cleanup(self):
        if self._finalizer.detach():
            _shutil.rmtree(self.name)

