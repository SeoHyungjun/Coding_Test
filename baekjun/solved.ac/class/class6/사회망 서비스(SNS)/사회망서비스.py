import sys
from collections import defaultdict
sys.setrecursionlimit(10 ** 9)

def solve(cur):
    dp[cur-1][0] = 1
    dp[cur-1][1] = 1

    for child in tree[cur]:
        if not dp[child-1][0]:
            solve(child)
            dp[cur-1][1] += min(dp[child-1][1], dp[child-1][2])
            dp[cur-1][2] += dp[child-1][1]

N = int(sys.stdin.readline())
tree = defaultdict(list)
# 0 -> visit, 1 -> early, 2 -> not early
dp = [[0]*3 for _ in range(N)]

for _ in range(N-1):
    u, v = map(int, sys.stdin.readline().split())
    tree[u].append(v)
    tree[v].append(u)

solve(1)
print(min(dp[0][1], dp[0][2]))