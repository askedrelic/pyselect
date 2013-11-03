========
pyselect
========

A Python library for easily getting user input from multiple items in a list, emulating the bash(1) select builtin function.

============
Usage
============

Pyselect wraps raw_input, more or less::

    In [1]: import pyselect
    In [2]: pyselect.select(['apples', 'oranges', 'bananas'])
    1) apples
    2) oranges
    3) bananas
    #? 2
    Out[2]: 'oranges'

But can also be used as a Python module, when scripting::

    $ python -m pyselect $(ls)
    1) LICENSE.txt
    2) build/
    3) dist/
    4) pyselect.egg-info/
    5) pyselect.py
    6) pyselect.pyc
    7) setup.py
    8) test.py
    #? 4
    pyselect.egg-info/

Or in a Bash pipe::

    $ ls | xargs python -m pyselect
    1) LICENSE.txt
    2) build/
    3) dist/
    4) pyselect.egg-info/
    5) pyselect.py
    6) pyselect.pyc
    7) setup.py
    8) test.py
    #? 5
    pyselect.py
    
============
Installation
============

Pyselect is available on Pypi::

    $ pip install pyselect

============
License
============

MIT, see LICENSE.txt
