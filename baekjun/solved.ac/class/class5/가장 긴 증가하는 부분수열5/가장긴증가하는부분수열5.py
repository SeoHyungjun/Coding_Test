import sys
from bisect import bisect_left

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

LIS = []
where = []
for i in range(N):
    if not LIS or arr[i] > LIS[-1]:
        LIS.append(arr[i])
        where.append(len(LIS)-1)
    else:
        tmp = bisect_left(LIS, arr[i])
        LIS[tmp] = arr[i]
        where.append(tmp)

print(len(LIS))
check = len(LIS)-1
answer = []
for i in range(len(arr)-1, -1, -1):
    if where[i] == check:
        answer.append(arr[i])
        check -= 1
print(*answer[::-1])