#!C:\Users\xcpro\ve1\Scripts\python.exe
# Copyright (c) Twisted Matrix Laboratories.
# See LICENSE for details.

import sys, os
extra = os.path.dirname(os.path.dirname(sys.argv[0]))
sys.path.insert(0, extra)
try:
    import _preamble
except ImportError:
    sys.exc_clear()
sys.path.remove(extra)

from twisted.conch.scripts.cftp import run
run()
