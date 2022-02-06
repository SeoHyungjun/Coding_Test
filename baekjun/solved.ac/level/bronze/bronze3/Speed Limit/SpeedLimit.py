import sys

while True:
    N = int(sys.stdin.readline())

    if N == -1:
        break

    total_miles = 0
    prev_time = 0

    for i in range(N):
        a, b = map(int, sys.stdin.readline().split())
        total_miles += a * (b - prev_time)
        prev_time = b

    print("%d miles"%(total_miles))