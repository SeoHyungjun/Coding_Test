import sys
from collections import defaultdict

U, N = map(int, sys.stdin.readline().split())

prices = defaultdict(int)
arr = []
for _ in range(N):
    name, price = sys.stdin.readline().split()
    prices[int(price)] += 1
    arr.append((name, int(price)))

min_key, min_value = 10001, 100001
for key, value in prices.items():
    if value < min_value:
        min_value = value
        min_key = key
    elif value == min_value:
        min_key = min(min_key, key)

for name, price in arr:
    if price == min_key:
        print(name, price)
        break