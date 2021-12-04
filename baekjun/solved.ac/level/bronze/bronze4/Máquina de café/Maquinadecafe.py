import sys

A = int(sys.stdin.readline())
B = int(sys.stdin.readline())
C = int(sys.stdin.readline())

print(min(2*B + 4*C, 2*A + 2*C, 4*A + 2*B))