import sys

a, b = map(int, sys.stdin.readline().split())
c = int(sys.stdin.readline())

print(a+b if a+b < 2*c else a+b-2*c)