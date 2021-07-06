import sys

N, S = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

start, end = 0, 0
sum = arr[start]
answer = float('inf')

while True:
    if sum >= S:
        answer = min(answer, end - start + 1)
        sum -= arr[start]
        start += 1

    else:
        end += 1
        if end >= N:
            break
        sum += arr[end]

print(answer if answer != float('inf') else 0)