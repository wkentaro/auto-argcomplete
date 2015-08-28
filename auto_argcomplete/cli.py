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
    parser.add_argument('--quote', help='with quote',
                        default=True, action='store_true', dest='with_quote')
    parser.add_argument('--no-quote', help='not show quote',
                        default=True, action='store_false', dest='with_quote')
    args = parser.parse_args()

    filename = os.path.expanduser(args.filename)
    show_desc = args.show_desc
    quote = "'" if args.with_quote else ""

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
    opt_args = parse_defaults(doc, section_name='optional arguments:')

    opt_descs = []
    for arg in opt_args:
        if arg.long:
            opt = arg.long
        elif arg.short:
            opt = arg.short
        desc = arg.description
        if args.show_desc and desc:
            opt_descs.append("{quote}{opt}:{desc}{quote}".format(opt=opt,
                                                                 desc=desc,
                                                                 quote=quote))
        else:
            opt_descs.append("{quote}{opt}{quote}".format(opt=opt,
                                                          quote=quote))
    print(' '.join(opt_descs))
