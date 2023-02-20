import sys

N, M = map(int, sys.stdin.readline().split())
cnt = [0] * (N + 1)

for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    cnt[a]+=1
    cnt[b]+=1

for i in range(1, N + 1):
    print(cnt[i])