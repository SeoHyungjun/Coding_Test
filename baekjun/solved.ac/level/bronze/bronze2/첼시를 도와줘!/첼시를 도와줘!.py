import sys

N = int(sys.stdin.readline())

for _ in range(N) :
    P = int(sys.stdin.readline())
    max_price, max_name = 0, ""
    for _ in range(P) :
        c, name = sys.stdin.readline().split()
        if int(c) <= max_price: continue
        max_price, max_name = int(c), name
    print(max_name)