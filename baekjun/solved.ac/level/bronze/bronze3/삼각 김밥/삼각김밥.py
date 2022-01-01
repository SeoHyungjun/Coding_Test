import sys

min_x, min_y = map(int, sys.stdin.readline().split())
answer = min_x/min_y

N = int(sys.stdin.readline())
for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())

    answer = min(answer, x/y)

print(answer*1000)