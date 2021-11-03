import sys

W, H, f, c, x1, y1, x2, y2 = map(int, sys.stdin.readline().split())

min_len = min(f, W-f)

if min_len < x1:
    small = 0
elif min_len < x2: #-> x1~min_len
    small = min_len - x1
else: # x2 < min_len -> x1~x2
    small = x2 - x1

print(W*H - (c+1) * (x2-x1 + small) * (y2 - y1))