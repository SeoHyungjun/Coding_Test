import sys
import math

def solve():
    distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    r_sum = r1 + r2
    r_diff = abs(r1 - r2)

    if distance == 0:
        if r1 == r2:
            return -1
        return 0

    if distance == r_sum or distance == r_diff:
        return 1
    if distance < r_sum and distance > r_diff:
        return 2
    return 0

for _ in range(int(sys.stdin.readline())):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())
    print(solve())