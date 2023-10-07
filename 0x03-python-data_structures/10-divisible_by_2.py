#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    resu = []
    for num in my_list:
        if num % 2 == 0:
            resu.append(True)
        else:
            resu.append(False)
    return resu
