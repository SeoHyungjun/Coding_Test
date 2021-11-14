import sys

A = int(sys.stdin.readline())
B = int(sys.stdin.readline())
C = int(sys.stdin.readline())
D = int(sys.stdin.readline())
E = int(sys.stdin.readline())
F = int(sys.stdin.readline())

print(A+B+C+D+E+F - min(A, B, C, D) - min(E, F))