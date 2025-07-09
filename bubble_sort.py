# Day 5: Bubble Sort Algorithm in Python

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap if the element found is greater
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Sample unsorted array
arr = [64, 34, 25, 12, 22, 11, 90]

print("Original array:", arr)
bubble_sort(arr)
print("Sorted array:", arr)
