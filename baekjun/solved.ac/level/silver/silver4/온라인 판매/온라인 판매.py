import sys

N, M = map(int, sys.stdin.readline().split())
prices = [int(sys.stdin.readline()) for _ in range(M)]
prices.sort()

answer = [0, 0]
for i, price in enumerate(prices):
    cur_price = min(N, M - i) * price

    if cur_price > answer[1]:
        answer = (price, cur_price)

print(*answer)