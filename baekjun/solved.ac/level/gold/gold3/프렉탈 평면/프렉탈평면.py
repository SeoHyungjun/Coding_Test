import sys

def dfs(len, x, y):
    if len == 1:
        return 0

    border = len / N
    if border * (N - K) / 2 <= x < border * (N + K) / 2 and border * (N - K) / 2 <= y < border * (N + K) / 2:
        return 1

    return dfs(border, x % border, y % border)

def solve():
    if s == 0:
        print(0)
        return
    
    len = N**s
    for i in range(R1, R2 + 1):
        for j in range(C1, C2 + 1):
            print(dfs(len, i, j), end = '')
        print()

s, N, K, R1, R2, C1, C2 = map(int, sys.stdin.readline().split())
solve()