import sys

A, B, C = map(int, sys.stdin.readline().split())

print(max(int(A*B/C), int(A/B*C)))