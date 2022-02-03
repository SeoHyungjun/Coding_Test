import sys

N = int(sys.stdin.readline())
for _ in range(N):
    X, Y = map(int, sys.stdin.readline().split())

    if X < Y:
        print('NO BRAINS')
    else:
        print('MMM BRAINS')