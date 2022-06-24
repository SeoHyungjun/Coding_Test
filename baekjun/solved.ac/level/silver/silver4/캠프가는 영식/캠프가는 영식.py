import sys

N, T = map(int, sys.stdin.readline().split())

answer = float('inf')
for _ in range(N):
    start_time, term, cnt = map(int, sys.stdin.readline().split())

    for i in range(cnt):
        cur_time = start_time + term * i
        if cur_time < T:
            continue

        answer = min(answer, cur_time - T)
        break

print(-1) if answer == float('inf') else print(answer)