#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-m', '--module')
parser.add_argument('-n', '--dry-run')
parser.add_argument('-k', '--kick-off')
parser.parse_args()
