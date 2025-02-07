import random

total_comparison = 0
pivot_method = None

def quicksort(arr, start_index, end_index):
    global total_comparison, pivot_method
    
    if start_index >= end_index or len(arr) <= 1:
        return

    # First element
    # pivot_position = start_index
    # pivot_method = "First element"
    
    # Last element
    # pivot_position = end_index
    # pivot_method = "Last Element"
    
    # Random pivot
    # pivot_position = random.randint(start_index, end_index)
    # pivot_method = "Random pivot"
    
    # Median of three
    # O(1)
    mid = int(((end_index - start_index) / 2) + start_index)
    c = sorted([arr[start_index], arr[mid], arr[end_index]])
    pivot_position = arr.index(c[1])
    pivot_method = "Median of three"
    
    buffer = arr[start_index]
    arr[start_index] = arr[pivot_position]
    arr[pivot_position] = buffer
    
    p = arr[start_index]
    j = start_index + 1
    for i in range(start_index + 1, end_index + 1):
        if arr[i] <= p:
            buffer = arr[j]
            arr[j] = arr[i]
            arr[i] = buffer
            j += 1
    buffer = arr[j - 1]
    arr[j - 1] = arr[start_index]
    arr[start_index] = buffer
    
    total_comparison += end_index - start_index
    
    quicksort(arr, start_index, j - 2)
    quicksort(arr, j, end_index)
    
    return arr

arr = []
with open("problem5_6.txt") as file:
    for line in file:
        number = int(line.strip())
        arr.append(number)

print(quicksort(arr, 0, len(arr) - 1))
print(pivot_method + " comparisons:", total_comparison)

