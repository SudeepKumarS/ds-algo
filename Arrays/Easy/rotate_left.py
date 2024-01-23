"""
Rotate the given array to left by given number
of place
"""


def rotate_array_to_left(nums: list, k: int) -> int:
    '''
    Function to rotate the array by k times left side
    '''
    rem = len(nums) - k
    temp = nums[:rem]
    nums = nums[rem:] + temp
    return nums


def another_approach(nums: list, k: int = 1) -> int:
    '''
    Function to rotate the array to the left by k times
    '''
    temp = nums[0]
    for i in range(1, len(nums)):
        nums[i - 1] = nums[i]
    nums[-1] = temp
    return nums


import random

ll = int(input("Please enter array length: "))

l = [random.choice([_ for _ in range(101)]) for _ in range(ll)]
print(l)
print(rotate_array_to_left(l, 3))
print(another_approach(l))
