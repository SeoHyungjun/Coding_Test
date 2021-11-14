import sys

a, b, c = map(int, sys.stdin.readline().split())

if max(a, b, c)**2 == a**2 + b**2 + c**2 - max(a, b, c)**2:
    print(1)
elif a == b and b == c:
    print(2)
else:
    print(0)