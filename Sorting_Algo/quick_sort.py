"""
Quick Sort: Pick a Pivot and place it in it's correct position

1. Pick a pivot and place it in it's correct position
2. Smaller on the left and larger on the right

Time Complexity: O(N*logN)
Space Complexity: O(1)

Better than Merge Sort in terms of Space Complexity but Merge Sort is also Important
"""

def partition(arr: list, low: int, high: int) -> tuple[int, list]:
    # Choosing the first element in the array as our pivot
    pivot = arr[low]
    # Choosing the two pointers as low and high
    i, j = low, high
    while (i < j):
        while (arr[i] <= pivot and i <= high - 1):
            i += 1
        while (arr[j] > pivot and j >= low + 1):
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[low], arr[j] = arr[j], arr[low]
    return j, arr


def quick_sort(arr: list, low: int, high: int) -> list:
    if low < high:
        # Doing a partition of the given array
        p_index, arr = partition(arr, low, high)
        # Applying same for the elements before the pivot point
        arr = quick_sort(arr, low, p_index - 1)
        # Applying same for the elements after the pivot point
        arr = quick_sort(arr, p_index + 1, high)
    return arr


import random

ll = int(input("Please enter array length: "))

l = [random.choice([_ for _ in range(101)]) for _ in range(ll)]
print(l)
print(quick_sort(l, 0, len(l) - 1))
