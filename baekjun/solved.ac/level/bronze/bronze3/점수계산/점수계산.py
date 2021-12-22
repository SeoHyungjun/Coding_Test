import sys

N = int(sys.stdin.readline())
point = list(map(int, sys.stdin.readline().split()))

for i in range(1, N):
    if point[i] == 1:
        point[i] += point[i-1]
    
print(sum(point))