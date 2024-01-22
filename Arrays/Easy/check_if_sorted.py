"""
Check if the given array is sorted.
"""


def check_if_sorted(arr: list) -> bool:
    '''
    Method to check if the given array is sorted
    '''
    for i in range(1, len(arr)):
        if arr[i] >= arr[i - 1]:
            pass
        else:
            return False
    return True


import random

ll = int(input("Please enter array length: "))

l = [random.choice([_ for _ in range(101)]) for _ in range(ll)]
l = [1, 6, 8, 9, 14, 32, 56]
print(l)
print(check_if_sorted(l))