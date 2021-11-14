import sys
import math

def solve(x, y):
    distance = y - x
    maxJump = int(math.sqrt(distance))

    if distance == maxJump**2:
        return 2 * maxJump - 1
    elif maxJump**2 < distance <= maxJump**2 + maxJump:
        return 2 * maxJump
    else:
        return 2 * maxJump + 1

T = int(sys.stdin.readline())
for _ in range(T):
    x, y = map(int, sys.stdin.readline().split())
    print(solve(x, y))