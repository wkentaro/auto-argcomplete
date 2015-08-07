===========
``autoarg``
===========

``autoarg`` is automatic shell completion generator for script
which uses argparse.

The behavior is like::

    $ python example/simple_script.py <TAB>
    $ python example/simple_script.py --
    --dry-run   --help      --kick-off  --module


`simple_script.py` is::

    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--module')
    parser.add_argument('-n', '--dry-run')
    parser.add_argument('-k', '--kick-off')
    parser.parse_args()


Installation
============

.. code-block:: sh

    $ pip install autoarg
