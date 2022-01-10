import sys

answer = [0, 0]
for i in range(5):
    point = sum(map(int, sys.stdin.readline().split()))
    if answer[1] < point:
        answer = [i+1, point]

print(*answer)