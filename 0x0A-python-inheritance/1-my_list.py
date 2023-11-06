#!/usr/bin/python3
"""Create MyList class"""


class MyList(list):
    """inherits list:
        Public instance method:
            def print_sorted(self)"""
    pass

    def print_sorted(self):
        """Sorte a list"""
        print(sorted(list(self)))