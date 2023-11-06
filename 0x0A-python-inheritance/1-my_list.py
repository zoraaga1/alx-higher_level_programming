#!/usr/bin/python3
"""Create MyList class"""


class MyList(list):
    """inherits list:
        Public instance method:
            def print_sorted(self)"""

    def print_sorted(self):
        """Prints the list,
                but sorted (ascending sort)"""
        print(sorted(self))
