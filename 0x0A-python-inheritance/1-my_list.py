#!/usr/bin/python3
"""Create MyList class"""


class MyList(list):
    """inherits from list:
        Public instance method:
            def print_sorted(self)"""
    pass
    def print_sorted(self):
        """Prints the list,
                but sorted (ascending sort)"""
        print(sorted(list(self)))
