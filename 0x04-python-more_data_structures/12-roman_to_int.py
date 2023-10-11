#!/usr/bin/python3

def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    
    roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    result = 0
    prev_value = 0

    for char in roman_string[::-1]:
        value = roman_values[char]

        if value < prev_value:
            result -= value
        else:
            result += value

        prev_value = value

    return result

# Test the function
roman_numeral = "MCMXCIV"  # Example: 1994
integer_value = roman_to_int(roman_numeral)
print(integer_value)  # Output: 1994
