import sys

A = int(sys.stdin.readline())
B = int(sys.stdin.readline())
C = int(sys.stdin.readline())
D = int(sys.stdin.readline())
P = int(sys.stdin.readline())

usage_a = P*A
usage_b = B if P <= C else B + (P-C)*D

print(min(P*A, B if P <= C else B + (P-C)*D))