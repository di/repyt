import os
import pwd
import sys
import argparse
import subprocess

try:
    # Location of run_with_reloader in the latest version of Werkzeug
    from werkzeug._reloader import run_with_reloader
except ImportError:
    # Old location of run_with_reloader
    from werkzeug.serving import run_with_reloader


def get_command():
    '''
    Return the command from the args supplied.
    '''
    parser = argparse.ArgumentParser(
        description='Automatically re-run Python commands when files change.')

    parser.add_argument(
        '--command',
        '-c',
        action='store',
        default=None,
        help='Specify any other shell command as a single string.')
    parser.add_argument(
        "args",
        nargs=argparse.REMAINDER,
        help='Arguments as if you were passing them to the `python` command.')

    op = parser.parse_args(sys.argv[1:])

    if op.command:
        return op.command
    elif op.args:
        return "python %s" % (" ".join(op.args))
    else:
        parser.print_usage()
        sys.stderr.write('repyt: error: too few arguments.\n')
        sys.exit(2)


def get_shell():
    '''
    Return the current shell.
    '''
    return os.environ.get('SHELL', pwd.getpwuid(os.getuid()).pw_shell)


def get_files():
    '''
    Get the files to monitor.
    '''
    matches = []
    for root, dirnames, filenames in os.walk('.'):
        for filename in filenames:
            matches.append(os.path.join(root, filename))
    return matches


def main():
    # Command-line entry point for setup.py install/develop
    command = get_command()
    shell = get_shell()
    files = get_files()

    run_with_reloader(
        lambda: subprocess.call(
            command,
            shell=True,
            executable=shell),
        extra_files=files)
