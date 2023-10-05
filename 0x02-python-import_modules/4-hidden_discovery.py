#!/usr/bin/python3
import hidden_4


def main():
    module_names = dir(hidden_4)
    module_names.sort()  # Sort the names alphabetically

    for name in module_names:
        if not name.startswith("__"):  # Filter out names starting with "__"
            print(name)


if __name__ == "__main__":
    main()
