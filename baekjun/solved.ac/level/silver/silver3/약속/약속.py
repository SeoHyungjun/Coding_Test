import sys

N = int(sys.stdin.readline())
arr = []
for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())
    arr.append(a - b)
arr.sort()

print(1) if len(arr) % 2 else print(abs(arr[N//2] - arr[N//2 - 1]) + 1)