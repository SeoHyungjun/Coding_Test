import sys

A, B = map(int, sys.stdin.readline().split())
C = int(sys.stdin.readline())

minuteDiv, minute = divmod(B + C, 60)
print((A + minuteDiv)%24, minute)