import sys

A, B, C = map(int, sys.stdin.readline().split())

if A == B or B == C or C == A:
    print('S')
elif A+B == C or B+C == A or A+C == B:
    print('S')
else:
    print('N')