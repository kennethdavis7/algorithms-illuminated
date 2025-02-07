import heapq
from datetime import datetime

start = datetime.now()

hl = [] 
hm = [] 
sum = 0  

with open("problem11_3.txt") as file:
    for line in file:
        number = int(line)

        if not hl or number <= -hl[0]:
            heapq.heappush(hl, -number) 
        else:
            heapq.heappush(hm, number) 

        if len(hl) > len(hm) + 1:
            heapq.heappush(hm, -heapq.heappop(hl))
        elif len(hm) > len(hl):
            heapq.heappush(hl, -heapq.heappop(hm))

        sum += -hl[0]

print(sum % 10000)

end = datetime.now()
td = (end - start).total_seconds() * 10**3
print(f"The time of execution of above program is : {td:.03f}ms")
