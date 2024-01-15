"""
Selection sort: The main principle of this is to select the minimum 
and swap it.

Time Complexity: O(n^2)

Time Complexity for Best, Average and Worst cases is O(n^2) 
"""

def selection_sort(arr: list[int]) -> list[int]:
    """
    Method to sort a list using selection sort algorithm
    """
    n = len(arr)
    # We just need to travese till last one element, as the last element will gets sorted automatically 
    for i in range(0, n - 1):
        min_v = i  # Assuming that the minimum value is at first index of array by default
        # Now we need to travese and find the minimum element and swap it.
        # The first iteration it (0, n); 2nd iter -> (1, n); 3rd iter -> (2, n) and so on....
        for j in range(i, n):
            # Checking if the array value at index i is greater than value at j, then changing min_v = j
            if arr[min_v] > arr[j]:
                min_v = j  # Now the minimum value is at index j
        # As we have the minimum value so,
        # swapping the value at min_v with value at i
        arr[min_v], arr[i] = arr[i], arr[min_v]
    # Finally, we have the sorted array
    return arr

import random

ll = int(input("Please enter array length: "))

l = [random.choice([_ for _ in range(101)]) for _ in range(ll)]
print(l)
print(selection_sort(l))




