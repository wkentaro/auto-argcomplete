#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import os
import sys
import re
import argparse
import subprocess
from subprocess import Popen, PIPE

import click

from .packages.docopt import parse_defaults, parse_args


def _check_inferable(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    is_inferable = False
    for line in lines:
        if re.search('import', line) and re.search('argparse', line):
            is_inferable = True
    return is_inferable


@click.group()
def cli():
    pass


@cli.command()
@click.argument('filename')
@click.option('--desc/--no-desc', 'show_desc', default=True)
@click.option('--quote/--no-quote', 'show_quote', default=True)
def options(filename, show_desc, show_quote):
    """Get options from python file with --help option."""

    filename = os.path.expanduser(filename)
    quote = "'" if show_quote else ""

    # check the file can have --help option
    if not _check_inferable(filename):
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
        if show_desc and desc:
            opt_descs.append("{quote}{opt}:{desc}{quote}".format(
                             opt=opt, desc=desc, quote=quote))
        else:
            opt_descs.append("{quote}{opt}{quote}".format(
                             opt=opt, quote=quote))
    print(' '.join(opt_descs))


@cli.command()
@click.argument('filename')
@click.option('--numbers', 'show_numbers', is_flag=True,
              help='show the numbers of args')
def args(filename, show_numbers):
    """Get args from python file with --help option."""

    filename = os.path.expanduser(filename)

    if not _check_inferable(filename):
        sys.exit(1)

    # run --help and collect args
    cmd = ['python', filename, '--help']
    proc = Popen(cmd, stdout=PIPE, stderr=PIPE)
    doc, stderr = proc.communicate()
    args = parse_args(doc, section_name='positional arguments:')
    arg_names = map(lambda x:x.name, args)
    if show_numbers:
        print(len(arg_names))
    else:
        print(' '.join(arg_names))
