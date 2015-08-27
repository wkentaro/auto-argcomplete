====================
``auto-argcomplete``
====================
.. image:: https://img.shields.io/pypi/v/auto-argcomplete.svg

``auto-argcomplete`` is automatic shell completion generator for script
which uses argparse.

The behavior is like::

    $ python example/simple_script.py <TAB>
    $ python example/simple_script.py --
    --dry-run   --help      --kick-off  --module

If you're using zsh::

    % python example/simple_script.py --
    --dry-run   -- display what to do
    --help      -- show this help message and exit
    --module    -- specify module name
    --kick-off

``example/simple_script.py`` is:

.. code-block:: python

    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--module', help='specify module name')
    parser.add_argument('-n', '--dry-run', help='display what to do')
    parser.add_argument('-k', '--kick-off')
    parser.parse_args()


**Nothing** to import in the script! :smile:

``auto-argcomplete`` can *automatically* understand the output of ``--help`` option,
so *automatically* supports all script which use argparse.


Installation
============

.. code-block:: sh

    $ pip install auto-argcomplete


Test
====

.. code-block:: sh

    $ nosetests -v auto_argcomplete


License
=======
| Copyright (C) 2015 Kentaro Wada
| Released under the MIT license
| http://opensource.org/licenses/mit-license.php
