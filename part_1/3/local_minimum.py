
def find_local_minimum(arr, row, column, minimum=None):
    mid_row = row // 2
    mid_column = column // 2


    if minimum is None:
        current_minimum = [arr[mid_row][mid_column], mid_row, mid_column]
    else:
        current_minimum = [arr[minimum[1]][minimum[2]], minimum[1], minimum[2]]
    
    for i in range(column):
        if current_minimum[0] > arr[mid_row][i]:
            current_minimum = [arr[mid_row][i], mid_row, i]
    
    for j in range(row):
        if current_minimum[0] > arr[j][mid_column]:
            current_minimum = [arr[j][mid_column], j, mid_column]


    is_local_minimum = True
    for v in range(-1, 2):
        for w in range(-1, 2):
            window_row = current_minimum[1] + v
            window_column = current_minimum[2] + w
            if 0 <= window_row < row and 0 <= window_column < column:
                if current_minimum[0] > arr[window_row][window_column]:
                    current_minimum = [arr[window_row][window_column], window_row, window_column]
                    is_local_minimum = False

    if is_local_minimum:
        return current_minimum[0]

    new_arr = []
    new_row = row // 2
    new_column = column // 2


    if current_minimum[1] < mid_row:  # Top half
        if current_minimum[2] < mid_column:  # Top-left quadrant
            new_arr = [row[:mid_column] for row in arr[:mid_row]]
            new_row = mid_row
            new_column = mid_column

            current_minimum[1] = current_minimum[1]
            current_minimum[2] = current_minimum[2]
        else:  # Top-right quadrant
            new_arr = [row[mid_column:] for row in arr[:mid_row]]
            new_row = mid_row
            new_column = column - mid_column

            current_minimum[1] = current_minimum[1]
            current_minimum[2] -= mid_column  
    else:  # Bottom half
        if current_minimum[2] < mid_column:  # Bottom-left quadrant
            new_arr = [row[:mid_column] for row in arr[mid_row:]]
            new_row = row - mid_row
            new_column = mid_column

            current_minimum[1] -= mid_row  
            current_minimum[2] = current_minimum[2]
        else:  # Bottom-right quadrant
            new_arr = [row[mid_column:] for row in arr[mid_row:]]
            new_row = row - mid_row
            new_column = column - mid_column

            current_minimum[1] -= mid_row  
            current_minimum[2] -= mid_column  

    return find_local_minimum(new_arr, len(new_arr), len(new_arr[0]), current_minimum)

arr = [
    [1100, 1150, 1200, 1250, 1300, 1350, 140 , 1450, 1500, 1550, 1600, 1650, 1700, 1750, 1800, 1850, 1900, 1950, 2000, 2050],
    [2100, 2150, 2200, 2250, 2300, 2350, 2400, 2450, 2500, 2550, 2600, 2650, 2700, 2750, 2800, 2850, 2900, 2950, 3000, 3050],
    [3100, 3150, 3200, 3250, 3300, 3350, 3400, 3450, 3500, 3550, 3600, 3650, 3700, 3750, 3800, 3850, 3900, 3950, 4000, 4050],
    [4100, 4150, 4200, 4250, 4300, 4350, 4400, 4450, 4500, 4550, 4600, 4650, 4700, 4750, 4800, 4850, 4900, 4950, 5000, 5050],
    [5100, 5150, 5200, 5250, 5300, 5350, 5400, 5450, 5500, 5550, 5600, 5650, 5700, 5750, 5800, 5850, 5900, 5950, 6000, 6050],
    [6100, 6150, 6200, 6250, 6300, 6350, 6400, 6450, 6500, 6550, 6600, 6650, 6700, 6750, 6800, 6850, 6900, 6950, 7000, 7050],
    [7100, 7150, 7200, 7250, 7300, 7350, 7400, 7450, 7500, 7550, 7600, 7650, 7700, 7750, 7800, 7850, 7900, 7950, 8000, 8050],
    [8100, 8150, 8200, 8250, 8300, 8350, 8400, 8450, 8500, 8550, 8600, 8650, 8700, 8750, 8800, 8850, 8900, 8950, 9000, 9050],
    [9100, 9150, 9200, 9250, 9300, 9350, 9400, 9450, 9500, 9550, 9600, 9650, 9700, 9750, 9800, 9850, 9900, 9950, 10000, 10050],
    [10100, 10150, 10200, 10250, 10300, 10350, 10400, 10450, 10500, 10550, 10600, 10650, 10700, 10750, 10800, 10850, 10900, 10950, 11000, 11050],
    [11100, 11150, 11200, 11250, 11300, 11350, 11400, 11450, 11500, 11550, 11600, 11650, 11700, 11750, 11800, 11850, 11900, 11950, 12000, 12050],
    [12100, 12150, 12200, 12250, 12300, 12350, 12400, 12450, 12500, 12550, 12600, 12650, 12700, 12750, 12800, 12850, 12900, 12950, 13000, 13050],
    [13100, 13150, 13200, 13250, 13300, 13350, 13400, 13450, 13500, 13550, 13600, 13650, 13700, 13750, 13800, 13850, 13900, 13950, 14000, 14050],
    [14100, 14150, 14200, 14250, 14300, 14350, 14400, 14450, 14500, 14550, 14600, 14650, 14700, 14750, 14800, 14850, 14900, 14950, 15000, 15050],
    [15100, 15150, 15200, 15250, 15300, 15350, 15400, 15450, 15500, 15550, 15600, 15650, 15700, 15750, 15800, 15850, 15900, 15950, 16000, 16050],
    [16100, 16150, 16200, 16250, 16300, 16350, 16400, 16450, 16500, 16550, 16600, 16650, 16700, 16750, 16800, 16850, 16900, 16950, 17000, 17050],
    [17100, 17150, 17200, 17250, 17300, 17350, 17400, 17450, 17500, 17550, 17600, 17650, 17700, 17750, 17800, 17850, 17900, 17950, 18000, 18050],
    [18100, 18150, 18200, 18250, 18300, 18350, 18400, 18450, 18500, 18550, 18600, 18650, 18700, 18750, 18800, 18850, 18900, 18950, 19000, 19050],
    [19100, 19150, 19200, 19250, 19300, 19350, 19400, 19450, 19500, 19550, 19600, 19650, 19700, 19750, 19800, 19850, 19900, 19950, 20000, 20050],
]

print(find_local_minimum(arr, 9, 10))

# My first attempt
# def find_local_minimum(arr, row, column, minimum=None):
#     mid_row = row // 2
#     mid_column = column // 2
    
#     if minimum is None:
#         current_minimum = [arr[mid_row][mid_column], mid_row, mid_column]
#     else:
#         current_minimum = [arr[minimum[1]][minimum[2]], minimum[1], minimum[2]]
    
#     for i in range(column):
#         if current_minimum[0] > arr[mid_row][i]:
#             current_minimum[0] = arr[mid_row][i]
#             current_minimum[1] = mid_row
#             current_minimum[2] = i
    
#     for j in range(row):
#         if current_minimum[0] > arr[j][mid_column]:
#             current_minimum[0] = arr[j][mid_column]
#             current_minimum[1] = j
#             current_minimum[2] = mid_column
    
#     is_local_minimum = True
#     for v in range(-1,2):
#         for w in range(-1,2):
#             window_row = current_minimum[1] + v
#             window_column = current_minimum[2] + w
#             if (window_row < row and window_row >= 0) and (window_column < column and window_column >= 0):
#                 if current_minimum[0] > arr[window_row][window_column]:
#                     current_minimum[0] = arr[window_row][window_column]
#                     current_minimum[2] = window_column
#                     current_minimum[1] = window_row
#                     is_local_minimum = False
                    
#     if is_local_minimum:
#         return current_minimum[0]
#     else:
#         new_arr = []
#         new_row = row // 2
#         new_column = column // 2
        
#         if mid_row > current_minimum[1] and mid_column > current_minimum[0]:
            
#             for k in range(row // 2):
#                 tmp = []
#                 for c in range(column // 2):
#                     tmp.append(arr[k][c])
#                 new_arr.append(tmp)
            
#         elif mid_row > current_minimum[1] and mid_column < current_minimum[0]:
            
#             new_row = row // 2
#             new_column = column - (column // 2)
#             for k in range(row // 2):
#                 tmp = []
#                 for c in range((column // 2) + 1, column):
#                     tmp.append(arr[k][c])
#                 new_arr.append(tmp)
            
#         elif mid_row < current_minimum[1] and mid_column > current_minimum[0]:
            
#             new_row = row - (row // 2)
#             new_column = column // 2
#             for k in range((row // 2) + 1, row):
#                 tmp = []
#                 for c in range(column // 2):
#                     tmp.append(arr[k][c])
#                 new_arr.append(tmp)
                
#         else:
            
#             new_row = row - (row // 2)
#             new_column = column - (column // 2)
#             for k in range((row // 2) + 1, row):
#                 tmp = []
#                 for c in range((column // 2) + 1, column):
#                     tmp.append(arr[k][c])
#                 new_arr.append(tmp)
            
#         find_local_minimum(new_arr, new_row, new_column, current_minimum)