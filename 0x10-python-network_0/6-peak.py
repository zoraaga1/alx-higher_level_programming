#!/usr/bin/python3
"""Function module"""


def find_peak(list_of_integers):
    if not list_of_integers:
        return None

    low, high = 0, len(list_of_integers) - 1

    while low < high:
        mid = (low + high) // 2

        # Check if mid is a peak
        if list_of_integers[mid] > list_of_integers[mid + 1]:
            # The peak is on the left side
            high = mid
        else:
            # The peak is on the right side (or mid is part of an ascending sequence)
            low = mid + 1

    # At the end of the loop, low and high will converge to a peak
    return list_of_integers[low]
