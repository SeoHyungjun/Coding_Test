import sys

N = int(sys.stdin.readline())
answer = 0
for _ in range(N):
    if sum(map(int, sys.stdin.readline().split())) >= 2:
        answer += 1

print(answer)