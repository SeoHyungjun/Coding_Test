import sys
import math

n,k = map(int, sys.stdin.readline().split())
arr = [[[],[]] for _ in range(7)]
for _ in range(n):
    s,y = map(int, sys.stdin.readline().split())
    arr[y][s].append(1)

answer = 0
for w,m in arr:
    answer += math.ceil(len(w)/k) + math.ceil(len(m)/k)
print(answer)