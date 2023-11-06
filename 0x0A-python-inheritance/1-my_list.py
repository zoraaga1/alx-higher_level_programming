#!/usr/bin/python3
"""Create MyList class"""


class MyList(list):
    """inherits from list:
        Public instance method:
            def print_sorted(self)"""
    def print_sorted(self):
        """Prints the list,
                but sorted (ascending sort)"""
        sorted_list = sorted(self)
        print(sorted_list)
