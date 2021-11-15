import sys

A, B = map(int, sys.stdin.readline().split())

if A != B:
    print(max(A, B))
else:
    print(A)