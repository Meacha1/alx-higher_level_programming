#!/usr/bin/python3
def find_peak(list_of_integers):
"""Finds a peak in a list of unsorted integers."""

    # Initialize the start and end indices.
    start = 0
    end = len(list_of_integers) - 1

    # Binary search for a peak.
    while start < end:
        mid = (start + end) // 2
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            start = mid + 1
        else:
            end = mid

    return list_of_integers[start]
