#!/usr/bin/env python

import argparse
import sys

def pex_new(args):
    print 'New'
    print args

def pex_install(args):
    print 'Install'
    print args

def pex_help(args):
    print 'Help'
    print args

def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()

    new_parser = subparsers.add_parser('new')
    new_parser.set_defaults(func=pex_new)
    new_parser.add_argument('template_name')
    new_parser.add_argument('directory')

    install_parser = subparsers.add_parser('install')
    install_parser.set_defaults(func=pex_install)
    install_parser.add_argument('location')
    install_parser.add_argument('template_name')

    help_parser = subparsers.add_parser('help')
    help_parser.set_defaults(func=pex_help)
    help_parser.add_argument('command')

    args = parser.parse_args()
    args.func(args)


if __name__ == '__main__':
    main()
