import sys
import math

L = int(sys.stdin.readline())
A = int(sys.stdin.readline())
B = int(sys.stdin.readline())
C = int(sys.stdin.readline())
D = int(sys.stdin.readline())

print(min(L - math.ceil(A / C), L - math.ceil(B / D)))