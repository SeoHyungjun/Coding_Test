import sys

N = int(sys.stdin.readline())
for _ in range(N):
    r, e, c = map(int, sys.stdin.readline().split())

    net_profit = e - c

    if r < net_profit:
        print("advertise")
    elif r > net_profit:
        print("do not advertise")
    else:
        print("does not matter")