#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from contextlib import contextmanager


@contextmanager
def redirect_stdout(stream):
    sys.stdout = stream
    try:
        yield
    finally:
        sys.stdout = sys.__stdout__
