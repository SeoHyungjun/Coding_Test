import sys

N = int(sys.stdin.readline())
A, B, C = map(int, sys.stdin.readline().split())

print(min(N, A) + min(N, B) + min(N, C))