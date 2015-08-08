====================
``auto-argcomplete``
====================

``auto-argcomplete`` is automatic shell completion generator for script
which uses argparse.

The behavior is like::

    $ python example/simple_script.py <TAB>
    $ python example/simple_script.py --
    --dry-run   --help      --kick-off  --module


``example/simple_script.py`` is

.. code-block:: python

    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--module')
    parser.add_argument('-n', '--dry-run')
    parser.add_argument('-k', '--kick-off')
    parser.parse_args()


**Nothing** to import in the script! :smile:

``auto-argcomplete`` can *automatically* understand the output of ``--help`` option,
so *automatically* supports all script which use argparse.


Installation
============

.. code-block:: sh

    $ pip install auto-argcomplete


License
=======
| Copyright (C) 2015 Kentaro Wada
| Released under the MIT license
| http://opensource.org/licenses/mit-license.php
