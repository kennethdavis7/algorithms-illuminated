import random

def quicksort(arr, start_index, end_index):
    if start_index >= end_index or len(arr) <= 1:
        return

    pivot_position = random.randint(start_index, end_index)
    
    buffer = arr[start_index]
    arr[start_index] = arr[pivot_position]
    arr[pivot_position] = buffer
    
    p = arr[start_index]
    j = start_index + 1
    for i in range(start_index + 1, end_index + 1):
        if arr[i][0] == p[0] and arr[i][1] < p[1]:
            p, arr[i] = arr[i], p
            arr[start_index] = p
        
        if arr[i][0] >= p[0]:
            buffer = arr[j]
            arr[j] = arr[i]
            arr[i] = buffer
            j += 1
    
    buffer = arr[j - 1]
    arr[j - 1] = arr[start_index]
    arr[start_index] = buffer
    
    quicksort(arr, start_index, j - 2)
    quicksort(arr, j, end_index)
    
    return arr

totalJobs = 0
jobs = []

with open("problem13_4.txt") as file:
    for line in file:
        split = line.split(" ")
        if len(split) == 1:
            totalJobs = int(split[0])
            continue
        weight = int(split[0])
        length = int(split[1])
        jobs.append((weight - length, weight, length))
        

quicksort(jobs, 0, len(jobs) - 1)

sum = 0
currentCompletionTime = 0
for job in jobs:
    currentCompletionTime += job[2]
    sum += job[1] * currentCompletionTime

print(sum)