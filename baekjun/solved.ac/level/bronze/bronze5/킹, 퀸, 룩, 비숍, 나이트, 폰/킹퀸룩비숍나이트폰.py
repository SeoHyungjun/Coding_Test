import sys

answer = [1, 1, 2, 2, 2, 8]
arr = list(map(int, sys.stdin.readline().split()))

print(*[answer[i] - arr[i] for i in range(len(answer))])