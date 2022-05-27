import sys
from math import gcd

T = int(sys.stdin.readline())
for _ in range(T):
    A, B = map(int, sys.stdin.readline().split())

    GCD = gcd(A, B)
    print(A*B//GCD)