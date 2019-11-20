#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
from urllib import request
import time

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""


def custom_sort(url):
    pattern = r'\-\w+\-(\w+)\.jpg$'
    match = re.search(pattern, url)
    if match:
        return match.group(1)
    return url


def read_urls(filename):
    """Returns a list of the puzzle urls from the given log file,
    extracting the hostname from the filename itself.
    Screens out duplicate urls and returns the urls sorted into
    increasing order."""
    urls = []
    pattern = r'"GET\s(.*puzzle.*)\sHTTP\/\d\.\d"'
    host = f"http://{filename.split('_')[1]}"

    with open(filename, 'r') as fp:
        line = fp.readline()
        while line:
            match = re.search(pattern, line)
            if match:
                path = f'{host}{match.group(1)}'
                if path in urls:
                    print(path)
                else:
                    urls.append(path)
            line = fp.readline()
    return sorted(urls, key=custom_sort)


def download_images(img_urls, dest_dir):
    """Given the urls already in the correct order, downloads
    each image into the given directory.
    Gives the images local filenames img0, img1, and so on.
    Creates an index.html in the directory
    with an img tag to show each local image file.
    Creates the directory if necessary.
    """
    if not os.path.exists(dest_dir):
        os.mkdir(dest_dir)

    img_paths = []
    for i, url in enumerate(img_urls):
        img_path = f'img{i + 1}'
        request.urlretrieve(url, os.path.join(dest_dir, img_path))
        img_paths.append(f'<img src="{img_path}">')
        time.sleep(1)  # wait for 1 second before go to next image

    with open(os.path.join(dest_dir, 'index.html'), 'w') as fp:
        fp.write(
            f"""<verbatim>
<html>
<body>
{''.join(img_paths)}
</body>
</html>"""
        )


def main():
    args = sys.argv[1:]

    if not args:
        print('usage: [--todir dir] logfile ')
        sys.exit(1)

    todir = ''
    if args[0] == '--todir':
        todir = args[1]
        del args[0:2]

    img_urls = read_urls(args[0])

    if todir:
        download_images(img_urls, todir)
    else:
        print('\n'.join(img_urls))


if __name__ == '__main__':
    main()
