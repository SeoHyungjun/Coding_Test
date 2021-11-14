import sys
import math

def ccw(a, b, c):
    return a[0]*b[1] + b[0]*c[1] + c[0]*a[1] - (b[0]*a[1] + a[0]*c[1] + c[0]*b[1])

# convex hull 알고리즘
def convex_hull():
    stack = []
    stack.append(arr[0])
    stack.append(arr[1])

    for i in range(2, N):
        while len(stack) >= 2:
            second = stack.pop()
            first = stack[-1]
            if (ccw(first, second, arr[i]) > 0):
                stack.append(second)
                break

        stack.append(arr[i])

    return len(stack)

N = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 시작점을 찾기 위해 y가 가장 작은 점을 찾는다. y가 같으면 x가 가장 작은 점
arr.sort(key = lambda x : (x[1], x[0]))
arr[1:] = sorted(arr[1:], key = lambda x : (math.atan2(x[1] - arr[0][1], x[0] - arr[0][0]), x[1], x[0]))
print(convex_hull())