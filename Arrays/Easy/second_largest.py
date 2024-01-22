"""
Find the second largest element in the given array
without sorting the list

Way of solving:
1. Try Brute Force
2. Try for Better
3. Then go for optimal solution
"""

def find_second_largest(arr: list) -> int:
    '''
    Method to return second largest element in the 
    given array
    
    :param arr: list
    :return int
    '''
    first_largest = arr[0]
    # Taking the value as -ve infinity
    second_largest = float('-inf')
    first_smallest = arr[0]
    second_smallest = float('inf')
    for i in range(len(arr)):
        if arr[i] > first_largest:
            # First storing the largest value in to the second_largest
            # variable and then replacing it's value
            second_largest = first_largest
            first_largest = arr[i]
        # Checking if the value
        if arr[i] > second_largest and arr[i] != first_largest:
            second_largest = arr[i]
        if arr[i] < first_smallest:
            second_smallest = first_smallest
            first_smallest = arr[i]
        if arr[i] < second_smallest and arr[i] != first_smallest:
            second_smallest = arr[i]
    return first_largest, second_largest, first_smallest, second_smallest


import random

ll = int(input("Please enter array length: "))

l = [random.choice([_ for _ in range(101)]) for _ in range(ll)]
print(l)
print(find_second_largest(l))