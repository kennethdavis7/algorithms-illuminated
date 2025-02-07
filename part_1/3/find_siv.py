def find_same_index_value(arr, start_index, end_index):
    if start_index == end_index:
        if arr[start_index] == start_index:
            return "A[" + str(start_index) + "] = " + str(arr[start_index]) 
        else:
            return "Not Found"
    mid = (((end_index - start_index) + 1) // 2) + start_index
    if mid == arr[mid]:
        return "A[" + str(mid) + "] = " + str(arr[mid]) 
    elif mid > arr[mid]:
        return find_same_index_value(arr, mid + 1, end_index)
    elif mid < arr[mid]:
        return find_same_index_value(arr, start_index, mid - 1)
    
arr = [0,4,5,6,7,8,9]
print(find_same_index_value(arr, 0, len(arr) - 1))