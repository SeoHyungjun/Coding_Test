import sys
import math

N, W, H = map(int, sys.stdin.readline().split())
max_length = math.sqrt(W**2 + H**2)

for _ in range(N):
    if int(sys.stdin.readline()) <= max_length:
        print('DA')
    else:
        print('NE')