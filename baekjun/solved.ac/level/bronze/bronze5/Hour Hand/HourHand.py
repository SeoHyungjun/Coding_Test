import sys

A = int(sys.stdin.readline())
B = int(sys.stdin.readline())
print(12 if (A+B)%12 == 0 else (A+B)%12 )