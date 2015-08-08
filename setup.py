#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
from __future__ import print_function
import os
import sys
import subprocess
import platform
from setuptools import setup, find_packages

this_dir = os.path.dirname(os.path.abspath(__file__))


def get_version():
    sys.path.insert(0, this_dir)
    from autoarg.version import __version__
    return __version__


def get_install_requires():
    req_file = os.path.join(this_dir, 'requirements.txt')
    with open(req_file) as f:
        required = f.readlines()
    return required


def get_data_files():

    def get_completion_install_location(shell):
        uname = platform.uname()[0]
        is_root = (os.geteuid() == 0)
        prefix = ''
        if is_root:
            # this is system install
            if uname == 'Linux':
                prefix = '/'
            elif uname == 'Darwin':
                prefix = '/usr'
        if shell == 'bash':
            location = os.path.join(prefix, 'etc/bash_completion.d')
        elif shell == 'zsh':
            location = os.path.join(prefix, 'share/zsh/site-functions')
        else:
            raise ValueError('unsupported shell: {0}'.format(shell))
        return location

    data_files = []
    loc = {'bash': get_completion_install_location(shell='bash'),
           'zsh': get_completion_install_location(shell='zsh')}
    files = {'bash': ['completion/autoarg-completion.bash'],
             'zsh': ['completion/_autoarg']}
    data_files.append((loc['bash'], files['bash']))
    data_files.append((loc['zsh'], files['zsh']))
    return data_files


# publish helper
if sys.argv[-1] == 'publish':
    for cmd in [
            'python setup.py register sdist upload',
            'git tag {}'.format(get_version()),
            'git push origin master --tag']:
        subprocess.check_call(cmd, shell=True)
    sys.exit(0)

long_description = """\
auto-argcomplete is automatic shell completion generator
for script which uses argparse.
auto-argcomplete can automatically understand the output of --help option,
so automatically supports all script which use argparse.
"""

setup(
    name='auto-argcomplete',
    version=get_version(),
    packages=find_packages(),
    description='Auto argument completion for script with argparse.',
    long_description=long_description,
    author='Kentaro Wada',
    author_email='www.kentaro.wada@gmail.com',
    url='http://github.com/wkentaro/auto-argcomplete',
    install_requires=get_install_requires(),
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
