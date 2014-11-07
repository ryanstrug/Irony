__author__ = 'Ryan Strug'

from sys import argv
from Parser import Parser
from Handler import Handler


if len(argv) == 2 and type(argv[1]) is str:
    if argv[1] == '-h':
        Handler.print_help()
    elif argv[1] == '-v':
        Handler.print_version()
    else:
        try:
            f = open(argv[1], 'r')
            p = Parser(f)
            p.count_objects()
            p.print_results()
            f.close()
        except FileNotFoundError:
            Handler.error(FileNotFoundError)
else:
    Handler.print_usage()