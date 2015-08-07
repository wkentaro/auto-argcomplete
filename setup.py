#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
from __future__ import print_function
import os
import sys
import imp
import subprocess
import platform
from setuptools import setup, find_packages


def get_version():
    return '0.1'

def get_data_files():

    def get_completion_install_location(shell):
        uname = platform.uname()[0]
        is_root = (os.geteuid() == 0)
        prefix = ''
        if shell == 'bash':
            if is_root and uname == 'Linux':
                prefix = '/'
            location = os.path.join(prefix, 'etc/bash_completion.d')
        elif shell == 'zsh':
            location = os.path.join(prefix, 'share/zsh/site-functions')
        else:
            raise ValueError('unsupported shell: {0}'.format(shell))
        return location

    location = {
        'bash': get_completion_install_location(shell='bash'),
        'zsh': get_completion_install_location(shell='zsh'),
        }
    comp_files = {
        'bash': [],
        'zsh': [
            'completion/_python',
            ],
        }
    data_files = [(location['bash'], comp_files['bash']),
                  (location['zsh'], comp_files['zsh'])]
    return data_files


# publish helper
if sys.argv[-1] == 'publish':
    for cmd in [
            'python setup.py register sdist upload',
            'git tag {}'.format(get_version()),
            'git push origin master --tag']:
        subprocess.check_call(cmd, shell=True)
    sys.exit(0)

setup(
    name='autoarg',
    version=get_version(),
    packages=find_packages(),
    description='auto args completion',
    author='Kentaro Wada',
    author_email='www.kentaro.wada@gmail.com',
    url='http://github.com/wkentaro/autoarg',
    install_requires=[''],
    license='MIT',
    keywords='utility',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX',
        'Topic :: Internet :: WWW/HTTP',
        ],
    entry_points={'console_scripts': ['autoarg=autoarg.cli:main']},
    data_files=get_data_files(),
    )
