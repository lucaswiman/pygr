#!/usr/bin/env python
"""
Pygr
====

Pygr is an open source software project used to develop graph database
interfaces for the popular Python language, with a strong emphasis
on bioinformatics applications ranging from genome-wide analysis of
alternative splicing patterns, to comparative genomics queries of
multi-genome alignment data.
"""
from __future__ import absolute_import, print_function

import os
import sys

from setuptools import setup, Extension

import pygr


def error(msg):
    "Fatal errors"
    print('*** error %s' % msg)
    sys.exit()

PYGR_NAME = "pygr"
PYGR_VERSION = pygr.__version__

if sys.version_info < (2, 3):
    error('pygr requires python 2.3 or higher')

CLASSIFIERS = """
Development Status :: 5 - Production/Stable
Operating System :: MacOS :: MacOS X
Operating System :: Microsoft :: Windows :: Windows NT/2000
Operating System :: OS Independent
Operating System :: POSIX
Operating System :: POSIX :: Linux
Operating System :: Unix
Programming Language :: Python
Topic :: Scientific/Engineering
Topic :: Scientific/Engineering :: Bio-Informatics
"""

# split into lines and filter empty ones
CLASSIFIERS = filter(None, CLASSIFIERS.splitlines())

# Setuptools should handle all this automatically
try:
    import pkg_resources
    pkg_resources.require('cython')
    ext = 'pyx'
except pkg_resources.DistributionNotFound:
    ext = 'c'
cmdclass = {}

# extension sources
seqfmt_src = [os.path.join('pygr', 'seqfmt.%s' % ext)]
cdict_src = [os.path.join('pygr', 'cgraph.c'),
             os.path.join('pygr', 'cdict.%s' % ext)]
nested_src = [os.path.join('pygr', 'intervaldb.c'),
              os.path.join('pygr', 'cnestedlist.%s' % ext),
              os.path.join('pygr', 'apps', 'maf2nclist.c')]


def main():
    setup(
        name = PYGR_NAME,
        version= PYGR_VERSION,
        description = \
'Pygr, a Python graph-database toolkit oriented primarily on bioinformatics',
        long_description = __doc__,
        author = "Christopher Lee",
        author_email='leec@chem.ucla.edu',
        url = 'http://code.google.com/p/pygr/',
        license = 'New BSD License',
        classifiers = CLASSIFIERS,

        packages = ['pygr', 'pygr.apps'],

        ext_modules = [
            Extension('pygr.seqfmt', seqfmt_src),
            Extension('pygr.cdict', cdict_src),
            Extension('pygr.cnestedlist', nested_src),
        ],

        cmdclass = cmdclass,
     )

if __name__ == '__main__':
    main()
