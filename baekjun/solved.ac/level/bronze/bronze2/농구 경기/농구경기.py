import sys
from collections import defaultdict

N = int(sys.stdin.readline())
players = defaultdict(int)
for _ in range(N):
    player = sys.stdin.readline().rstrip()
    players[player[0]] += 1

answer = []
for key in players:
    if players[key] >= 5:
        answer.append(key)

if not answer:
    print("PREDAJA")
else:
    answer.sort()
    print(''.join(answer))