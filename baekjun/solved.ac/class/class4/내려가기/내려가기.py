import sys

N = int(sys.stdin.readline())

max_dp = min_dp = gr = list(map(int, sys.stdin.readline().split()))
for _ in range(N-1):
    gr = list(map(int, sys.stdin.readline().split()))
    max_dp = [gr[0] + max(max_dp[0], max_dp[1]), gr[1] + max(max_dp[0], max_dp[1], max_dp[2]), gr[2] + max(max_dp[1], max_dp[2])]
    min_dp = [gr[0] + min(min_dp[0], min_dp[1]), gr[1] + min(min_dp[0], min_dp[1], min_dp[2]), gr[2] + min(min_dp[1], min_dp[2])]
    
print(max(max_dp), min(min_dp))