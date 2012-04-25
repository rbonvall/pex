#!/usr/bin/env python

import optparse
import sys


def main():
    parser = optparse.OptionParser()
    (options, args) = parser.parse_args()

    if not args:
        parser.print_help()
        sys.exit(-1)

    command, rest = args[0], args[1:]


if __name__ == '__main__':
    main()
