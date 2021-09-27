import sys
sys.setrecursionlimit(10**6)

def palindrom(start, end):
    global dp
    if dp[start][end]:
        return 1

    dp[start][end] = 1 if arr[start] == arr[end] and palindrom(start+1, end-1) else 0
    return dp[start][end]

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())

dp = [[0]*N for _ in range(N)]
for i in range(N):
    dp[i][i] = 1
    if i < N-1 and arr[i] == arr[i+1]:
        dp[i][i+1] = 1

for i in range(M):
    start, end = map(int, sys.stdin.readline().split())
    print(palindrom(start-1, end-1))