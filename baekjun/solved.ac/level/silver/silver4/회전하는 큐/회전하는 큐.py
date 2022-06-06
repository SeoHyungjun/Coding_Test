import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
arr = deque([i for i in range(1, N+1)])
index = list(map(int, input().split()))

cnt = 0
for i in index:
    while arr[0] != i:
        arr.rotate(-1) if arr.index(i) <= len(arr)//2 else arr.rotate(1)            
        cnt += 1
        
    arr.popleft()

print(cnt)