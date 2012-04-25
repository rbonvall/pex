#!/usr/bin/env python

import argparse
import sys


def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()

    new_parser = subparsers.add_parser('new')
    new_parser.add_argument('template_name')
    new_parser.add_argument('directory')

    install_parser = subparsers.add_parser('install')
    install_parser.add_argument('location')
    install_parser.add_argument('template_name')

    help_parser = subparsers.add_parser('help')
    help_parser.add_argument('command')

    ns = parser.parse_args()
    print ns


if __name__ == '__main__':
    main()
