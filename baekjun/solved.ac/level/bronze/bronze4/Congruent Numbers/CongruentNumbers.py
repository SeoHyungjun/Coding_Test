import sys

p1, q1, p2, q2 = map(int, sys.stdin.readline().split())

if p1 * p2 % (q1 * q2 * 2) == 0:
    print(1)
else:
    print(0)