import sys

N = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().split()))

lis = [1 for _ in range(len(arr))]
lds = [1 for _ in range(len(arr))]

for i in range(len(arr)):
    for j in range(i):
        if arr[i] > arr[j]:
            lis[i] = max(lis[i], lis[j]+1)
arr.reverse()
for i in range(len(arr)):
    for j in range(i):
        if arr[i] > arr[j]:
            lds[i] = max(lds[i], lds[j]+1)

lds.reverse()
answer = 0
for i in range(N):
    answer = max(answer, lis[i] + lds[i])

print(answer - 1)