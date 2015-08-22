================
auto-argcomplete
================

**auto-argcomplete** is automatic shell completion generator
for script which uses argparse.

The code is open source, and `available on github`_.

.. _available on github: http://github.com/wkentaro/auto-argcomplete


.. toctree::
   :maxdepth: 1

   installation
   testing
   license


The function is very simple, it can *automatically* complete script's options::

    $ python example/simple_script.py <TAB>
    $ python example/simple_script.py --
    --dry-run   --help      --kick-off  --module

If you're using zsh::

    % python example/simple_script.py --
    --dry-run   -- display what to do
    --help      -- show this help message and exit
    --module    -- specify module name
    --kick-off


**Nothing** to import in the script!

**auto-argcomplete** can *automatically* understand the output of ``--help`` option,
so *automatically* supports all script which use argparse.

