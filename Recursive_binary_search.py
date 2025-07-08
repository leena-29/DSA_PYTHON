# Day 4: Binary Search Algorithm using Recursion in Python

def binary_search_recursive(arr, target, low, high):
    if low > high:
        return -1  # Target not found

    mid = (low + high) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, high)
    else:
        return binary_search_recursive(arr, target, low, mid - 1)

# Sample sorted array
arr = [2, 6, 13, 21, 36, 47, 63, 81]
target = 47

# Perform recursive binary search
result = binary_search_recursive(arr, target, 0, len(arr) - 1)

# Output result
if result != -1:
    print(f"Element {target} found at index {result}.")
else:
    print(f"Element {target} not found in the array.")
