#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None

    max_value = my_list[0]  # Initialize max_value with the first element

    for num in my_list:
        if num > max_value:
            max_value = num  # Update max_value if a larger number is found

    return max_value
