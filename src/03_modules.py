"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
print('Command line arguments in sys.argv: ')
for i in sys.argv:
    print(i)

# Print out the OS platform you're using:
print('OS platform: ', sys.platform)

# Print out the version of Python you're using:
print('Python version: ', sys.version)

import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
print('Current process ID: ', os.getpid())

# Print the current working directory (cwd):
print('Current working directory: ', os.getcwd())

# Print out your machine's login name
print('Login name: ', os.getlogin())
