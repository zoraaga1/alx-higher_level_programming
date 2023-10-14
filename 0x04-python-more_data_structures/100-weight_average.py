#!/usr/bin/python3

def weight_average(my_list=[]):
    if not my_list:
        return 0  # Return 0 if the list is empty

    total_score = 0
    total_weight = 0

    for score, weight in my_list:
        total_score += score * weight
        total_weight += weight

    if total_weight == 0:
        return 0  # Avoid division by zero

    weighted_average = total_score / total_weight
    return weighted_average
