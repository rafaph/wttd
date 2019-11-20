#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Problem description:
# https://developers.google.com/edu/python/exercises/copy-special


import glob
import os
import shutil
import subprocess
import sys

"""Copy Special exercise

"""


# Write functions and modify main() to call them

def iter_special_paths(directory):
    for filename in glob.glob(os.path.join(directory, '*__*__.*')):
        yield os.path.abspath(filename)


def copy_to(paths, directory):
    if not os.path.exists(directory):
        os.mkdir(directory)

    for path in paths:
        shutil.copy(path, directory)


def zip_to(paths, zippath):
    args = [
        'zip',
        '-j',
        zippath,
        *paths
    ]
    print(f"Command I'm going to do:{' '.join(args)}")
    try:
        subprocess.check_output(args)
    except subprocess.CalledProcessError as error:
        print(error.output.decode('utf-8'))
        return error.returncode
    return 0


def main():
    # This basic command line argument parsing code is provided.
    # Add code to call your functions below.

    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args = sys.argv[1:]
    if not args:
        print("usage: [--todir dir][--tozip zipfile] dir [dir ...]")
        sys.exit(1)

    # todir and tozip are either set from command line
    # or left as the empty string.
    # The args array is left just containing the dirs.
    todir = ''
    if args[0] == '--todir':
        todir = args[1]
        del args[0:2]

    tozip = ''
    if args[0] == '--tozip':
        tozip = args[1]
        del args[0:2]

    if len(args) == 0:
        print("error: must specify one or more dirs")
        sys.exit(1)

    # Call your functions

    for directory in args:
        paths = iter_special_paths(directory)
        if todir:
            copy_to(paths, todir)
        elif tozip:
            returncode = zip_to(paths, tozip)
            if returncode != 0:
                sys.exit(returncode)
        else:
            for special_path in paths:
                print(special_path)


if __name__ == "__main__":
    main()
