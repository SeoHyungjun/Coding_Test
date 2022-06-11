import sys

N, K = map(int, sys.stdin.readline().split())
arr = [i for i in range(1, N+1)]

answer = []
index = 0
for _ in range(N):
    index += K - 1
    if index >= len(arr):
        index %= len(arr)

    answer.append(str(arr.pop(index)))

print('<' + ', '.join(answer) + '>')