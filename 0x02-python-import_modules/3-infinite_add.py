#!/usr/bin/python3
import sys


def main():
    args = sys.argv[1:]  # Exclude the script name itself
    result = 0
    arg = 0

    for arg in args:
        result += int(arg)

    print(result)


if __name__ == "__main__":
    main()
