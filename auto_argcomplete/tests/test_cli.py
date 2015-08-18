#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
from StringIO import StringIO

from nose.tools import assert_equal

import auto_argcomplete.cli
from auto_argcomplete.utils import redirect_stdout


def test_main():
    this_dir = os.path.dirname(os.path.abspath(__file__))
    sys.argv = ['auto_argcomplete',
                os.path.join(this_dir, '../../example/simple_script.py')]
    f = StringIO()
    with redirect_stdout(f):
        auto_argcomplete.cli.main()
    output = f.getvalue().strip()
    assert_equal(len(output.split("' ")), 4)
