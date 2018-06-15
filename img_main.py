#!/usr/bin/env python

# Copyright 2015 Fetch Robotics Inc.
# Author: Sandeep Chahal

## @file img_main.py takes details from cmd_tr.py and rescales using res.py

from cmd_tr import CmdInpt as Term
from res import ResizingImagesDetails as Rs


def main():

    # request_type, resize_scale, path_for_image, desired_path_for_image = \
    details, fi_or_ig, path_to_image, path_to_destination, resizing_scale = Term().storing_arguments()
    Rs(resizing_scale).image_func(fi_or_ig, path_to_image, path_to_destination)


if __name__ == '__main__':
    main()