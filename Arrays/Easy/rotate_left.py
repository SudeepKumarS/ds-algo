"""
Rotate the given array to left by given number
of place
"""


# Rotate the array to the left by 1 time
def rotate_array_left(nums: list) -> int:
    '''
    Function to rotate the array to the left by 1 time
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
print(rotate_array_left(l))
