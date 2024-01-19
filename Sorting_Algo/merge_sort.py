""""
Merge Sort: Divide and Merge Strategy 

Dividing the given array into smaller parts
Merge the smaller to get a sorted array

Time Complexity: O(N*logN)
Space Complexity: ~O(N)
"""

def merge(first_half: list, second_half: list):
    """"
    Method to merge the given array
    """
    temp = []
    left = 0
    right = 0
    # Run until both the arrays are not exhausted
    while (left < len(first_half) and right < len(second_half)):
        if first_half[left] <= second_half[right]:
            temp.append(first_half[left])
            left += 1
        else:
            temp.append(second_half[right])
            right += 1
    
    # If any of them are exhausted then
    while (left < len(first_half)):
        temp.append(first_half[left])
        left += 1
    while (right < len(second_half)):
        temp.append(second_half[right])
        right += 1
    # temp.extend(first_half[left:])
    # temp.extend(second_half[right:])
    return temp


def merge_sort(arr: list) -> list:
    """
    Method to perform a merge sort on a given array
    """
    if (len(arr) <= 1):
        return arr
    mid = len(arr) // 2
    first_half = merge_sort(arr[:mid])
    # Second Half of array
    second_half = merge_sort(arr[mid:])
    # Merging the above divided arrays
    return merge(first_half, second_half)


import random

ll = int(input("Please enter array length: "))

l = [random.choice([_ for _ in range(101)]) for _ in range(ll)]
print(l)
print(merge_sort(l))

