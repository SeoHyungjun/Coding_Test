import sys

A, B = map(int, sys.stdin.readline().split())
print(1 if A*(100-B)/100 < 100 else 0)