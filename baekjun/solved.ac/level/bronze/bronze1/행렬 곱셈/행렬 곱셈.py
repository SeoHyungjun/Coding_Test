import sys

N, M = map(int, sys.stdin.readline().split())
A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
M, K = map(int, sys.stdin.readline().split())
B = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]

for i in range(N):
    for j in range(K):
        sum = 0
        for k in range(M):
            sum += A[i][k] * B[k][j]
        print(sum, end = ' ')
    print()