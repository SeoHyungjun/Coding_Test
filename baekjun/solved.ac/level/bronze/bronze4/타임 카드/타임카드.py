import sys

def solve(A):
    h, m, s = A[3] - A[0], A[4] - A[1], A[5] - A[2]
    if s < 0:
        s = 60 + s
        m -= 1
    if m < 0:
        m = 60 + m
        h -= 1
    if h < 0:
        h = 24 + h

    print(h, m ,s)

A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))
C = list(map(int, sys.stdin.readline().split()))

solve(A)
solve(B)
solve(C)
