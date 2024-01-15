"""
Bubble sort: The main principle is to push the maximum to last by swaping the
Adjacent elements.

Time Complexity: O(n^2) for Average and Worst case
O(N) for Best case as we have used a check for swap
"""

def bubble_sort(arr: list[int]) -> list[int]:
    """
    Method to sort a list using Bubble sort algorithm
    """
    n = len(arr)
    # Here, we'll start from 1st iter -> (0, n-1); 2nd iter -> (0, n-2)
    for i in range(n-1, 0, -1):
        swapped = False
        for j in range(i):
            # Checking the adjacent value and swapping, if value is maximum
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True

        # If nothing gets swapped, we can break or return the array
        if not swapped:
            break
    return arr

import random

ll = int(input("Please enter array length: "))

l = [random.choice([_ for _ in range(101)]) for _ in range(ll)]
print(l)
print(bubble_sort(l))