import random

def find_pivot(arr):
    n = len(arr)
    if n == 1:
        return arr[0]
    
    medians = []
    for j in range(0, n, 5):
        group = sorted(arr[j:j + 5]) 
        medians.append(group[len(group) // 2])
    
    return find_pivot(medians)

def DSelect(arr, i):
    n = len(arr)
    
    if n == 1:
        return arr[0]

    pivot = find_pivot(arr)
    
    pivot_index = arr.index(pivot)
    
    arr[0], arr[pivot_index] = arr[pivot_index], arr[0]
    
    p = arr[0]
    j = 1
    for k in range(1, n):
        if arr[k] <= p:
            arr[j], arr[k] = arr[k], arr[j]
            j += 1
            
    new_pivot_position = j - 1
    arr[0], arr[new_pivot_position] = arr[new_pivot_position], arr[0]
    
    target_index = i - 1
    
    if target_index < pivot_index:  
        return DSelect(arr[:pivot_index], i)
    elif target_index == pivot_index: 
        return pivot
    else:  
        return DSelect(arr[(pivot_index + 1):], i - pivot_index - 1)


def RSelect(arr, i, start_index=0, end_index=None):
    if end_index is None:
        end_index = len(arr) - 1

    if start_index == end_index:
        return arr[start_index]

    pivot_position = random.randint(start_index, end_index)
    arr[start_index], arr[pivot_position] = arr[pivot_position], arr[start_index]
    
    p = arr[start_index]
    j = start_index + 1
    for k in range(start_index + 1, end_index + 1):
        if arr[k] <= p:
            arr[j], arr[k] = arr[k], arr[j]
            j += 1


    new_pivot_position = j - 1
    arr[start_index], arr[new_pivot_position] = arr[new_pivot_position], arr[start_index]

    target_index = i - 1

    if new_pivot_position == target_index:
        return arr[new_pivot_position]
    elif new_pivot_position > target_index:
        return RSelect(arr, i, start_index, new_pivot_position - 1) 
    else:
        return RSelect(arr, i, new_pivot_position + 1, end_index)

# arr = []
# with open("problem6_5test1.txt") as file:
#     for line in file:
#         number = int(line.strip())
#         arr.append(number)


with open('100000pi.txt', 'r') as file:
    pi_digits = file.read().strip()

pi_digits = pi_digits.replace('.', '')

arr = [pi_digits[i:i+10] for i in range(0, len(pi_digits), 10)]

arr = arr[:100000]

print("RSelect result: " + str(RSelect(arr, len(arr)/2)))
print("DSelect result: " + str(DSelect(arr, len(arr)/2)))

