import sys
from itertools import combinations

N = int(sys.stdin.readline())

max_sum = -1
for i in range(1, N+1):
    cards = list(map(int, sys.stdin.readline().split()))

    combi_arr = combinations(cards, 3)
    max_card_sum = sum(max(combi_arr, key=lambda x: (sum(x) % 10))) % 10

    if max_card_sum > max_sum:
        max_sum = max_card_sum
        answer = i
    elif max_card_sum == max_sum:
        answer = max(answer, i)

print(answer)