#!/usr/bin/env python

# Copyright 2015 Fetch Robotics Inc.
# Author: Sandeep Chahal

## @file cmd_tr.py  takes the arguments

import argparse


class CmdInpt:
    """takes input from terminal"""
    def __init__(self):
        self.argument_parser = argparse.ArgumentParser(prog="RESIZING EXISTING APRILTAGS",
                                                       usage='[-i,-f,-d, --rs '
                                                             '(new size),--p (path), --ds (destination) ]',
                                                       formatter_class=argparse.RawDescriptionHelpFormatter,
                                                       description="This module gives you the re-sized picture,"
                                                                   " mainly created for apriltags")

    def storing_arguments(self):
        """ 
            -v(verbose),-q(quiet)
            -i(image): bool, -f(file); bool, --d(default): bool
            -p(path_to_image/file); None/string
            -ds(path_to_destination); None/string

            returns bool, string, None/String, None/String, int
            """
        """
        # optional argument for verbose or quiet
        self.argument_parser.add_argument("-v", "--verbose", help="displays additional details on screen",
                                     action="store_true")  # show details
        self.argument_parser.add_argument("-q", "--quiet", help="hides additional details from on screen",
                                     action="store_true")  # hide details"""

        # optional argument for choosing image/file/default
        self.argument_parser.add_argument("-i", "--image", help="to convert single image",
                                          action="store_true")
        self.argument_parser.add_argument("-f", "--file", help="to convert all images of a file/folder",
                                          action="store_true")
        self.argument_parser.add_argument("--d", "--default",
                                          help="if -i or -f is not specified by default it takes"
                                          "'image.png' from current file, not to be used with -it or -f option",
                                          action="store_false")

        # optional arguments scale resize factor
        self.argument_parser.add_argument("--rs", help="resize by scale, takes only"
                                                       " integer as scale. default_value = 200",
                                          type=int, default=200)

        # optional path to image and desired path to store image
        self.argument_parser.add_argument("--p", help="path to image",
                                          type=str, default=None)  # resize by scale
        self.argument_parser.add_argument("--ds", help="path to file",
                                          type=str, default=None)  # resize by scale

        args = self.argument_parser.parse_args()
        rs = args.rs
        """# checking edge cases
        if args.verbose and args.quiet:
            print "-v and -q options selected, showing details"
        elif not args.verbose and not args.quiet:
            print "-v and -q not specified \n hiding details"""

        if args.file and args.image:
            print "file and single images can't be selected at same time\n terminating program"

        """
        if args.verbose:
            print "displaying operation details"
            if args.file:
                return True, "file", args.p, args.ds, rs
            elif args.image:
                return True, "image", args.p, args.ds, rs
            else:
                return True, "default", args.p, args.ds, rs

        else:
            print "hiding operation details"
            if args.file:
                return False, "file", args.p, args.ds, rs
            elif args.image:
                return False, "image", args.p, args.ds, rs
            else:
                return False, "default", args.p, args.ds, rs"""

        if args.file:
            return True, "file", args.p, args.ds, rs
        elif args.image:
            return True, "image", args.p, args.ds, rs
        else:
            return True, "default", args.p, args.ds, rs