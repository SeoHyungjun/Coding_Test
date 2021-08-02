import sys
from bisect import bisect_left

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

lis = [arr[0]]
for i in range(1, N):
    if lis[-1] < arr[i]:
        lis.append(arr[i])
    elif lis[-1] >= arr[i]:
        lis[bisect_left(lis, arr[i])] = arr[i]

print(len(lis))