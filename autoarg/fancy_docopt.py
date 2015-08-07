#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
from docopt import Option


def parse_section(name, source):
    pattern = re.compile('^([^\n]*' + name + '[^\n]*\n?(?:[ \t].*?(?:\n|$))*)',
                         re.IGNORECASE | re.MULTILINE)
    return [s.strip() for s in pattern.findall(source)]


def parse_defaults(doc, section_name=None):
    if section_name is None:
        section_name = 'options:'

    defaults = []
    for s in parse_section(section_name, doc):
        _, _, s = s.partition(':')
        split = re.split('\n[ \t]*(-\S+?)', '\n' + s)[1:]
        split = [s1 + s2 for s1, s2 in zip(split[::2], split[1::2])]
        options = [Option.parse(s) for s in split if s.startswith('-')]
        defaults += options
    return defaults
