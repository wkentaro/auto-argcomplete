#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import os
import sys
import re
import argparse
import subprocess
from subprocess import Popen, PIPE

from .packages.docopt import parse_defaults


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', help='python filename')
    parser.add_argument('--description', help='show description',
                        default=True, action='store_true', dest='show_desc')
    parser.add_argument('--no-description', help='not show description',
                        default=True, action='store_false', dest='show_desc')
    args = parser.parse_args()

    filename = os.path.expanduser(args.filename)
    show_desc = args.show_desc

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

    opt_descs = []
    for arg in args:
        if arg.long:
            opt = arg.long
        elif arg.short:
            opt = arg.short
        desc = arg.description
        if show_desc and desc:
            opt_descs.append("'{opt}:{desc}'".format(opt=opt, desc=desc))
        else:
            opt_descs.append("'{opt}'".format(opt=opt))
    print(' '.join(opt_descs))
