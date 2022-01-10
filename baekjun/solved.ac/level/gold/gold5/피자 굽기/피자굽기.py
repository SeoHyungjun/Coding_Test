import sys
from bisect import bisect_left

D, N = map(int, sys.stdin.readline().split())
oven = list(map(int, sys.stdin.readline().split()))
pizza = list(map(int, sys.stdin.readline().split()))

for i in range(1, D):
    oven[i] = min(oven[i-1], oven[i])
oven = oven[::-1]

cnt = 0
last = -1

for i in range(N):
    index = bisect_left(oven, pizza[i], lo=last+1)

    if cnt < N and index >= D:
        last = -1
        break

    if index < D:
        last = index
        cnt += 1

if last == -1:
    print(0)
else:
    print(D - last)