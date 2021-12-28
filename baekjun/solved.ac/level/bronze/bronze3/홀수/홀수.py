import sys

sum_odd = 0
min_odd = float('inf')

for _ in range(7):
    num = int(sys.stdin.readline())

    if num % 2 != 0:
        sum_odd += num
        min_odd = min(min_odd, num)

if sum_odd == 0:
    print(-1)
else:
    print(sum_odd)
    print(min_odd)