import sys

A, B, C = map(int, sys.stdin.readline().split())

if C - B <= 0:
    print(-1)
else:
    breakEvenpoint = A / (C - B)
    print(int(breakEvenpoint) + 1)