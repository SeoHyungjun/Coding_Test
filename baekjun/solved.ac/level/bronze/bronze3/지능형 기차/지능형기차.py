import sys

tmp = 0
answer = 0

for _ in range(4):
    a, b = map(int, sys.stdin.readline().split())
    tmp += b - a
    answer = max(answer, tmp)

print(answer)