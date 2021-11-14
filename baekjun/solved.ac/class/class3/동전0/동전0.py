import sys

N, K = map(int, sys.stdin.readline().split())
coins = []

for _ in range(N):
    coins.append(int(sys.stdin.readline()))

coins.reverse()

answer = 0
for coin in coins:
    if K == 0:
        break
    answer =  answer + K//coin
    K %= coin

print(answer)