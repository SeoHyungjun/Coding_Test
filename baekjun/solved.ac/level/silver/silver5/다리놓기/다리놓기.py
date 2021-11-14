# 2021-03-16 16:19 -> 16:45

import sys
from itertools import combinations

def mCn(n, m):
    if n == 0:
        return 1

    if n > m-n:
        n = m-n
    ans = 1
    for i in range(m, m-n, -1):
        ans *= i
    div = 1
    for i in range(1, n+1):
        div *= i

    return ans//div


n = int(sys.stdin.readline())

for _ in range(n):
    n, m = map(int, sys.stdin.readline().split())

    print(mCn(n, m))