#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import subprocess

from nose.tools import assert_equal

import auto_argcomplete.cli
from auto_argcomplete.utils import redirect_stdout


def test_options():
    this_dir = os.path.dirname(os.path.abspath(__file__))
    auto_argcomplete = os.path.join(this_dir, '../../auto_argcomplete_r')
    script = os.path.join(this_dir, '../../example/simple_script.py')
    cmd = [auto_argcomplete, 'options', script, '--no-desc', '--no-quote']
    output = subprocess.check_output(cmd).strip()
    assert_equal(output, '--help --module --dry-run --kick-off')


def test_args():
    this_dir = os.path.dirname(os.path.abspath(__file__))
    auto_argcomplete = os.path.join(this_dir, '../../auto_argcomplete_r')
    script = os.path.join(this_dir, '../../example/simple_script.py')
    cmd = [auto_argcomplete, 'args', script]
    output = subprocess.check_output(cmd).strip()
    assert_equal(output, 'src dest')
