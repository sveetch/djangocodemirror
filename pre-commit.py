#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
A pre commit hook to check watched files

Install : Put this file at ".git/hooks/pre-commit" or just make a symbolic link to it

Usage : If any watched file doesn't have a minified version in the predicted files for 
        commit, the commit is aborted. Assume that the minified version have the ".min" 
        extension in his filename just before the last original extension.

Searching for minified version will do something like this :

    foo.js > foo.min.js
    bar.css > bar.min.css
    morefnu > morefnu.min

"""
import os, subprocess, sys

MINIFIED_EXTENSION = "min" # Extension to assume for minified version
# Watched files by this hooks, files that are not in this list will 
# never be worried about
# Edit this to append your watched files to care of.
# Paths are relative to the root of the repository.
WATCHED_FILES = (
    'djangocodemirror/djangocodemirror.min.css',
    'djangocodemirror/djangocodemirror.min.js',
)

def has_minified_file(filename, tracked):
    """
    Check if the file has a minified version in the commit
    """
    minified_filename = os.path.splitext(filename)
    root, ext = os.path.splitext(filename)
    minified_filename = [root, MINIFIED_EXTENSION]
    if ext:
        minified_filename.append(ext[1:])
    minified_filename = ".".join(minified_filename)
    if minified_filename not in tracked:
        return False
    return True

#
if __name__ == "__main__":
    # Get the list of changed files wich are predicted in the commit
    p = subprocess.Popen(['git', 'diff-index', '--cached', '--name-only', 'HEAD'], stdout=subprocess.PIPE)
    out, err = p.communicate()
    # Crawl the status lines to find added or modified files
    tracked_files = [item_status for item_status in out.splitlines()]
    # Check for watched files in the commit
    err = False
    for item in tracked_files:
        if item in WATCHED_FILES and not has_minified_file(item, tracked_files):
            err = True
            print u"Watched file has no minified version (or not updated) : {0}".format(item)
    # Abort commit if error has been finded
    if err:
        print "Commit is aborted (you can use the '--no-verify' option to bypass this warning)"
        sys.exit(1)
    sys.exit(0)
