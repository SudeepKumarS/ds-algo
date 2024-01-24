"""
Rotate the given array to the left by given number
"""


# Brute force approach
def rotate(nums: list, k: int) -> list:
    '''
    Function to rotate the array to the left by given number
    '''
    n = len(nums)
    k = k % n
    temp = nums[:k]
    j = 0
    for i in range(k, n):
        nums[i - k] = nums[i]
    for j in range(n-k, n):
        nums[j] = temp[j - n + k]
    return nums
    
    
import random

ll = int(input("Please enter array length: "))
d = int(input("Please enter number of rotations: "))

l = [random.choice([_ for _ in range(101)]) for _ in range(ll)]

print(l)
print(rotate(l, d))