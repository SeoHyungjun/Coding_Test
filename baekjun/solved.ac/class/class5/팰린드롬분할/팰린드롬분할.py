import sys

S = sys.stdin.readline().rstrip()

dp = [ [0]*len(S) for _ in range(len(S)) ]

for i in range(len(S)):
    dp[i][i] = 1

for i in range(len(S)-1):
    if S[i] == S[i+1]:
        dp[i][i+1] = 1

for i in range(2, len(S)):
    for j in range(len(S)-i):
        if S[j] == S[j + i] and dp[j+1][j+i-1]:
            dp[j][j+i] = 1

answer = [0] * (len(S)+1)
for i in range(1, len(S)+1):
    answer[i] = answer[i-1] + 1
    for j in range(1, i+1):
        if dp[j-1][i-1]:
            answer[i] = min(answer[j-1]+1, answer[i])

print(answer[len(S)])
