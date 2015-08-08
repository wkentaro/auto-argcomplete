#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import re
import subprocess
from subprocess import Popen, PIPE

from .fancy_docopt import parse_defaults


def main():
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        sys.exit(1)

    filename = os.path.expanduser(filename)

    # check the file imports argparse
    with open(filename, 'r') as f:
        lines = f.readlines()
    found_argparse = False
    for line in lines:
        if re.search('import', line) and re.search('argparse', line):
            found_argparse = True
    if not found_argparse:
        sys.exit(1)

    # run --help and collect args
    cmd = ['python', filename, '--help']
    proc = Popen(cmd, stdout=PIPE, stderr=PIPE)
    doc, stderr = proc.communicate()
    args = parse_defaults(doc, section_name='optional arguments:')

    for arg in args:
        opt = ''
        if arg.long:
            opt = arg.long
        elif arg.short:
            opt = arg.short
        print(opt)
