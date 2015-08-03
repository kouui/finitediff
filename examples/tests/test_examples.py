# -*- coding: utf-8 -*-

"""
Tests all examples in Python subprocesses.
Note: if setting PYTHONPATH environment variable
for py.test: make sure paths are absolute.
"""

import glob
import os
import subprocess
import sys

import pytest


tests = glob.glob(os.path.join(os.path.dirname(__file__), '../*.py'))


@pytest.mark.parametrize('pypath', tests)
def test_examples(pypath):
    p = subprocess.Popen(
        ['python3' if sys.version_info.major == 3 else 'python', pypath],
        cwd=os.path.join(os.path.dirname(__file__), '..'))
    assert p.wait() == 0  # SUCCESS==0
