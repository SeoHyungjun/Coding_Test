import sys

A, B, C = map(int, sys.stdin.readline().split())

print(max(B-A, C-B)-1)