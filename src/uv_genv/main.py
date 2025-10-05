#!/usr/bin/env python3

import argparse

from .cmd.create import cmd_create
from .cmd.list import cmd_list
from .cmd.remove import cmd_remove

def main():
    parser = argparse.ArgumentParser(prog="genvs", description="Manage global envs with uv")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # genvs create <name> [--python <version>]
    create_parser = subparsers.add_parser("create", help="Create a new global environment")
    create_parser.add_argument("name", help="Name of the environment")
    create_parser.add_argument("--python", help="Python version to be installed", required=False)
    create_parser.set_defaults(func=cmd_create)

    # genvs remove <name>
    remove_parser = subparsers.add_parser("remove", help="remove a specific global environment")
    remove_parser.add_argument("name", help="Name of the environment")
    remove_parser.set_defaults(func=cmd_remove)

    # genvs list
    list_parser = subparsers.add_parser(
        "list", help="List global environments with their Python version and last modified date"
    )
    list_parser.set_defaults(func=cmd_list)

    args = parser.parse_args()
    args.func(args)
