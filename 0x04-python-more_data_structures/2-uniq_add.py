#!/usr/bin/python3

def uniq_add(my_list=[]):
    uniq_set = set()
    sum = 0
    for item in my_list:
        if item not in uniq_set:
            sum += item
            uniq_set.add(item)
    return sum
