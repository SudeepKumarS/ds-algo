"""
To find the largest element in the given array.
"""

def find_largest(arr: list) -> int:
    '''
    Method to find the largest element in the 
    given array
    '''
    largest = arr[0]
    for i in arr:
        if i > largest:
            largest = i
    return largest

import random

ll = int(input("Please enter array length: "))

l = [random.choice([_ for _ in range(101)]) for _ in range(ll)]
print(l)
print(find_largest(l))