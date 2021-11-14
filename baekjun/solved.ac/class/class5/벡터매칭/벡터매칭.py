import sys
from itertools import combinations
from math import sqrt
import sys
sys.setrecursionlimit(2500)

answer = float('inf')
def find(cnt, index, sum_x, sum_y):
    global answer

    if index < N:
        if cnt == N//2:
            answer = min(answer, sqrt(sum_x**2 + sum_y**2))

        else:
            
                find(cnt, index+1, sum_x, sum_y)
                sum_x -= 2*point[index][0]
                sum_y -= 2*point[index][1]
                find(cnt+1, index+1, sum_x, sum_y)

T = int(sys.stdin.readline())

for _ in range(T):
    answer = float('inf')
    N = int(sys.stdin.readline())
    point = []
    x_total, y_total = 0, 0

    for _ in range(N):
        x, y = map(int, sys.stdin.readline().split())
        x_total += x
        y_total += y

        point.append((x, y))

    find(0, 0, x_total, y_total)
    print(answer)