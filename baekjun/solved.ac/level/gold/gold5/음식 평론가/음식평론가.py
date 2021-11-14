import sys

def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

N, M = map(int, sys.stdin.readline().split())

print(M - gcd(N, M))