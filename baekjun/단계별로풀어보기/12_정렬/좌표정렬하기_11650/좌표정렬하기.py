import sys

n = int(sys.stdin.readline())
arr = []

for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))
    
arr.sort(key = lambda x: (x[0], x[1]))

for x, y in arr:
    print(x, y)