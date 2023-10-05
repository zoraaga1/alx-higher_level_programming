#!/usr/bin/python3
import sys


def arg_list(arg):
    n_arg = len(arg)

    if n_arg == 0:
        print("0 arguments.")
    else:
        if n_arg == 1:
            print("{:d} argument:".format(n_arg))
            print(f"1: {arg[0]}")
        else:
            print("{:d} arguments:".format(n_arg))
            for i, arg in enumerate(arg, start=1):
                print(f"{i}: {arg}")


if __name__ == "__main__":
    arg = sys.argv[1:]
    arg_list(arg)
