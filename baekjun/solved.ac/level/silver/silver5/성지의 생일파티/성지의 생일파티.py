import sys

N = int(sys.stdin.readline())
arr = sorted([int(sys.stdin.readline()) for _ in range(N)])

for i, cur in enumerate(arr):
    if i >= cur:
        print(i+1)
        break