"""
Insertion sort: The main principle is to take an element and place it in the correct
position.

Time Complexity: O(n^2) for Average and Worst case
O(N) for Best case as we'll not use the inner loop to swap the elements if they are already sorted 
"""

def insetion_sort(arr: list[int]) -> list[int]:
    """
    Method to sort a list using Insertion sort algorithm
    """
    n = len(arr)
    # Here, we'll start from 0 till the last element of array
    for i in range(n):
        # Let's assume j is i
        j = i
        # Run and swap the element till the previous element
        # is less than the current element, i.e; it reaches the correct position 
        while j > 0 and (arr[j -1] > arr[j]):
            arr[j -1], arr[j] = arr[j], arr[j -1]
            j -= 1
    return arr
        
import random

ll = int(input("Please enter array length: "))

l = [random.choice([_ for _ in range(101)]) for _ in range(ll)]
print(l)
print(insetion_sort(l))