import sys

A, B = map(int, sys.stdin.readline().split())

print(int((max(A, B) * (max(A, B) + 1) - min(A, B) * (min(A, B) - 1)) / 2))