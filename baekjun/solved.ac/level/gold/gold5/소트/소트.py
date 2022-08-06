import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
S = int(sys.stdin.readline())

for i in range(N-1):
    if S <= 0:
        break

    max_value, index = arr[i], i
    for j in range(i+1, min(N, i+1+S)):
        if max_value < arr[j]:
            max_value, index = arr[j], j

    S -= index - i
    for j in range(index, i, -1):
        arr[j] = arr[j-1]
    arr[i] = max_value

print(*arr)