import sys

N, C = map(int, sys.stdin.readline().split())
check = [0] * (C+1)
cycle = {int(sys.stdin.readline()) for _ in range(N)}

if 1 in cycle:
    print(C)
else:
    for c in cycle:
        for i in range(c, C+1, c):
            check[i] = 1

    print(sum(check))