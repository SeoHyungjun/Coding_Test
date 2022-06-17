import sys

N = int(sys.stdin.readline())
arr = set(sorted([int(sys.stdin.readline()) for _ in range(N)]))

max_cnt = 0
for key in arr:
    cnt = 0
    for i in range(5):
        if key + i in arr:
            cnt += 1

    max_cnt = max(max_cnt, cnt)

print(5 - max_cnt)