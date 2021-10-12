import sys

N, M = map(int, sys.stdin.readline().split())
print(int(((N-M)**2)**0.5))