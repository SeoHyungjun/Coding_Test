import sys
from collections import defaultdict

def gcd(a, b):
    if not b:
        return a
    return gcd(b, a%b)

def solve(i):
    cnt = 0

    tmp_arr = point[:]
    tmp_arr[0], tmp_arr[i] = tmp_arr[i], tmp_arr[0]

    dic = defaultdict(int)

    for i in range(1, N):
        x, y = tmp_arr[i][0] - tmp_arr[0][0], tmp_arr[i][1] - tmp_arr[0][1]
        _gcd = abs(gcd(x, y))
        dic[(x//_gcd, y//_gcd)] += 1

    for key in dic.keys():
        cur_x, cur_y = key
        if (-cur_y, cur_x) in dic:
            cnt += dic[key] * dic[((-cur_y, cur_x))]

    return cnt
    
N = int(sys.stdin.readline())

point = []
for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    point.append((x, y))

answer = 0
for i in range(N):
    answer += solve(i)

print(answer)