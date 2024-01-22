"""
Remove duplicates in-place from a sorted array
"""

def remove_duplicates_from_sorted(arr: list) -> list:
    '''
    Function to remove duplicates from the give sorted array
    '''
    cur_uniq, j = 0, 1
    while j < len(arr):
        if arr[j] != arr[cur_uniq]:
            arr[cur_uniq + 1] = arr[j]
            cur_uniq += 1
        j += 1
    return arr[:cur_uniq + 1]


import random

ll = int(input("Please enter array length: "))

l = [random.choice([_ for _ in range(101)]) for _ in range(ll)]
print(l)
print(remove_duplicates_from_sorted([1, 6, 6, 7, 8, 9, 14, 14, 32, 32, 56]))
