#!/usr/bin/env python

from setuptools import setup, find_packages
import pyselect

setup(
    name                 = 'pyselect',
    version              = pyselect.__version__,
    description          = 'A Python library for easily getting user input form multiple items in a list, emulating the Bash(1) builtin select.',
    long_description     = open('README.rst').read() + '\n\n' + open('HISTORY.rst').read(),

    author               = pyselect.__author__,
    author_email         = 'askedrelic@gmail.com',
    url                  = 'https://github.com/askedrelic/pyselect',
    license              = open("LICENSE.txt").read(),

    # packages           = ['pyselect'],
    py_modules           = ['pyselect'],
    include_package_data = True,
    # test_suite         = 'tests',

    classifiers          = (
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        # 'Programming Language :: Python :: 3.3',
        # 'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ),
)
