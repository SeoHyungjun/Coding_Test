import sys

N, T, C, P = map(int, sys.stdin.readline().split())
print((N-1)//T * C * P)