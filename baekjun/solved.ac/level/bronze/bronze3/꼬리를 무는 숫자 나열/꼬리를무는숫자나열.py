import sys

A, B = map(int, sys.stdin.readline().split())
A -= 1
B -= 1

print(abs(B//4 - A//4) + abs(B%4-A%4))