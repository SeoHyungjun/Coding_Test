import sys

N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

for i in range(1, N):
    arr[i] += arr[i-1]

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())

    if i == 1:
        print(arr[j-1])
    else:
        print(arr[j-1] - arr[i-2])

