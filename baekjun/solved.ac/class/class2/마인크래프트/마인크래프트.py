import sys

n, m, b = map(int, sys.stdin.readline().split())
floor = {}
time = float('inf')
min_floor = 0

for _ in range(n):
    for i in list(map(int, sys.stdin.readline().split())):
        if i in floor:
            floor[i] += 1
        else:
            floor[i] = 1

for i in range(max(floor.keys()) + 1, max(min(floor.keys())-1, -1), -1):
    get_block = 0
    put_block = 0
    for j in floor.keys():
        if i < j:
            get_block += floor[j] * (j-i)
        elif i > j:
            put_block += floor[j] * (i-j)

    if put_block <= get_block + b:
        if time > 2*get_block + put_block:
            time = 2*get_block + put_block
            min_floor = i
        
        elif time == 2*get_block + put_block and min_floor < i:
            min_floor = i

print(str(time) + ' ' + str(min_floor))