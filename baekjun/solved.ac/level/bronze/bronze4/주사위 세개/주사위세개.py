import sys

A, B, C = map(int, sys.stdin.readline().split())

if A == B and B == C:
    print(10000 + A*1000)
elif A == B or B == C or C == A:
    if A == B:
        print(1000 + A*100)
    elif B == C:
        print(1000 + B*100)
    else:
        print(1000 + C*100)
else:
    print(max(A, B, C)*100)