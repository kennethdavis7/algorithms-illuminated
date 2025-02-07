from math import ceil

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

def weighted_median(x, w, n):
    if n == 1:
        return x[0]
    elif n == 2:
        if w[0] == w[1]:
            return [x[0], x[1]]
        elif w[0] < w[1]:
            return w[1]
        else:
            return w[0]
    else:
        median_x = DSelect(x, int(ceil(len(x)/2)))
        
        pivot_position = x.index(median_x)
        
        x[0], x[pivot_position] = x[pivot_position], x[0]
        w[0], w[pivot_position] = w[pivot_position], w[0]
        

        p = x[0]
        j = 1
        for k in range(1, n):
            if x[k] <= p:
                x[j], x[k] = x[k], x[j]
                w[j], w[k] = w[k], w[j]
                j += 1
                
        new_pivot_position = j - 1
        x[0], x[new_pivot_position] = x[new_pivot_position], x[0]
        w[0], w[new_pivot_position] = w[new_pivot_position], w[0]
        
        W = {
            "total": 0,
            'L': 0,
            'R': 0
        }
        
        for i in range(0, new_pivot_position):
            W['L'] += w[i]
            
        for j in range(new_pivot_position + 1, n):
            W['R'] += w[j]
        
        for v in range(0, n):
            W['total'] += w[v]
        
        half_w = W['total'] / 2
        
        if W['L'] < half_w and W['R'] == half_w:
            return [x[new_pivot_position], x[new_pivot_position + 1]]
        elif W['L'] == half_w and W['R'] < half_w:
            return [x[new_pivot_position - 1], x[new_pivot_position]]
        elif W['L'] <= half_w and W['R'] <= half_w:
            return x[new_pivot_position]
        elif W['L'] > half_w:
            w[new_pivot_position] += W['R']
            new_x = x[:new_pivot_position + 1]
            new_w = w[:new_pivot_position + 1]
            return weighted_median(new_x, new_w, len(new_x))
        else:
            w[new_pivot_position] += W['L']
            new_x = x[new_pivot_position:]
            new_w = w[new_pivot_position:]
            return weighted_median(new_x, new_w, len(new_x))
        
        
x = [1,2,3,4,5]
w = [.15, .1, .2, .3, .25]

# x = [1, 2, 3, 4]
# w = [.49, .01, .25, .25]

print(weighted_median(x,w,len(x)))