#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        integer_value = int(value)
        print("{:d}".format(integer_value))
        return True
    except (ValueError, TypeError) as e:
        sys.stderr.write("Exception: " + str(e) + "\n")
        return False
