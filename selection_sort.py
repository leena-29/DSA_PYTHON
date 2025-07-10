# Day 6: Selection Sort Algorithm in Python

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Find the minimum element in remaining unsorted array
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Sample unsorted array
arr = [29, 10, 14, 37, 13]

print("Original array:", arr)
selection_sort(arr)
print("Sorted array:", arr)
