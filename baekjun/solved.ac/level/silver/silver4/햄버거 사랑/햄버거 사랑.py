import sys

N, M, T = map(int, sys.stdin.readline().split())
if N > M:
    N, M = M, N

min_leave_time = float('inf')
burger_sum = 0
for i in range(T//N, -1, -1):
    avail_M = (T - i * N) // M
    leave_time = T - i * N - avail_M * M

    if leave_time < min_leave_time:
        min_leave_time = leave_time
        burger_sum = i  + avail_M
    elif leave_time ==min_leave_time:
        burger_sum = max(burger_sum, i + avail_M)

print(burger_sum, min_leave_time)