repyt
=====

Automatically re-run Python commands when files change.

Installation
============

::

    pip install repyt

Usage
=====

::

    repyt [-h] [--command COMMAND] [args]

Where::

    COMMAND             Any command to execute in the shell, as a string. This
                        doesn't even have to be a Python command!
    args                Arguments as you would normally pass to the `python`
                        command.
    -h or --help        Show this help message and exit.

Example
=======

Use it just like you would use the :code:`python` command:

::

    repyt hello_world.py

Including args is totally fine:

::

    repyt hello_world.py --world="Earth"

This is equivalent to:

::

    repyt -c 'python hello_world.py --world="Earth"'

The command arg doesn't even have to be a Python command:

::

    repyt -c 'echo "Yo Adrian! I did it!"'

Description
===========

repyt detects changes in the current directory and sub-directories, and re-runs
your Python script, application, or any other command when files are changed by
you or your editor.

It kindly ignores hidden files and a bunch of other stuff that probably isn't
important.

You should use it just like you use the :code:`python` command, if possible.

Contact
=======

:On PyPI:
    http://pypi.python.org/pypi/repyt/

:Souce:
    https://github.com/di/repyt

:Issues:
    https://github.com/di/repyt/issues
