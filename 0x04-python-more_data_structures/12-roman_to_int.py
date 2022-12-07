#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    romanD = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    romanN = 0
    for j in range(len(roman_string)):
        if j > 0 and romanD[roman_string[j]] > romanD[roman_string[j - 1]]:
            romanN += romanD[roman_string[j]] - 2 * \
                    romanD[roman_string[j - 1]]
        else:
            romanN += romanD[roman_string[j]]
    return romanN
