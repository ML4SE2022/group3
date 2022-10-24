#!/usr/bin/env python

import sys

while True:
    print("Please enter a number:")
    try:
        number = int(sys.stdin.readline())
        print("You entered:", number)
    except ValueError:
        print("That was not a number!")