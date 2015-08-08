#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import re
import subprocess

from .fancy_docopt import parse_defaults


def main():
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        sys.exit(1)

    cmd = ['python', filename, '--help']
    doc = subprocess.check_output(cmd)
    args = parse_defaults(doc, section_name='optional arguments:')

    for arg in args:
        opt = ''
        if arg.long:
            opt = arg.long
        elif arg.short:
            opt = arg.short
        print(opt)