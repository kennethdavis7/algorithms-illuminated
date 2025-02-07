def find_max(arr, n):
    if n == 1:
        return arr[0]
    if n == 2:
        if arr[0] > arr[1]:
            return arr[0]
        else:
            return arr[1]
    mid = n // 2
    if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
        return arr[mid]
    elif arr[mid] < arr[mid - 1] and arr[mid] > arr[mid + 1]:
        return find_max(arr[:mid], mid)
    else:
        return find_max(arr[mid:n], n - mid)

arr = [100, 150, 200, 250, 240, 220, 180, 120]
print(find_max(arr, len(arr)))