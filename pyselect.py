# -*- coding: utf-8 -*-

__title__ = 'pyselect'
__version__ = '0.1.0'
__author__ = 'Matthew Behrens'
__license__ = 'MIT'
__copyright__ = 'Copyright 2013 Matthew Behrens'

import sys

def select(options=None):
    if not options:
        return None
    width = len(str(len(options)))
    for x,option in enumerate(options):
        print '{:{width}}) {}'.format(x+1,option, width=width )

    response = raw_input('{:>{width}} '.format('#?', width=width+1)).strip()
    try:
        response = int(response) - 1
    except ValueError:
        return None
    if response < 0:
        return None
    if response > len(options):
        return None
    return options[response]

def main(args=None):
    if args is None:
        args = sys.argv[1:]
    response = select(args)
    if response:
        print response

if __name__ == '__main__':
    main()
    # print select(xrange(10))
    # print select('apple orange banana'.split())
    # print select('foo bar bar'.split())
