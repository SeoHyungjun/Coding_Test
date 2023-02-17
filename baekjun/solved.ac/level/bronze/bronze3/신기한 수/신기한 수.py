import sys

N = int(sys.stdin.readline())

cnt = 0
for i in range(1, N+1):
    t = sum([int(c) for c in str(i)])
    if i % t != 0: continue
    cnt += 1

print(cnt)