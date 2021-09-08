import sys

def solve():
    for i in range(N):
        for j in range(i+1, N):
            if arr[i] + arr[j] < W:
                dp[arr[i] + arr[j]] = arr[i]

    for i in range(1, (W-1)//2 + (W-1)%2):
        if not dp[i] or not dp[W-i]:
            continue

        if len({dp[i], i - dp[i], dp[W - i], W - i - dp[W - i]}) == 4:
            return 'YES'

    return 'NO'

W, N = map(int, sys.stdin.readline().split())
arr = sorted(list(map(int, sys.stdin.readline().split())))
dp = [False] * W

print(solve())