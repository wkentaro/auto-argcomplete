#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('src')
parser.add_argument('dest')
parser.add_argument('-m', '--module', help='specify module name')
parser.add_argument('-n', '--dry-run', help='display what to do')
parser.add_argument('-k', '--kick-off')
parser.parse_args()
