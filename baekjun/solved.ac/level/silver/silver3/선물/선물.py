import sys

N, L, W, H = map(int, sys.stdin.readline().split())
start, end = 0, max(L, W, H)

for _ in range(100):
    mid = (start + end) / 2

    if (L//mid) * (W//mid) * (H//mid) >= N:
        start = mid
    else:
        end = mid

print("%.10f"%end)