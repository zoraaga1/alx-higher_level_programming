#!/usr/bin/python3

def magic_calculation(a, b):
    add = 0
    sub = 0

    if a < b:
        add = magic_calculation_102.add(a, b)
        for i in range(4, 6):
            add = magic_calculation_102.add(add, i)

        return add

    return magic_calculation_102.sub(a, b)
