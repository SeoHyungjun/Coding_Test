import sys
from collections import defaultdict
sys.setrecursionlimit(int(1e5))
input = sys.stdin.readline

def ccw(a, b, c):
    return a[0]*b[1] + b[0]*c[1] + c[0]*a[1] - (a[0]*c[1] + b[0]*a[1] + c[0]*b[1])

def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])
    return parent[a]

def union(a, b):
    a = find(a)
    b = find(b)
    if a <= b:
        parent[b] = a
    else:
        parent[a] = b

def checkLine(a, b):
    if ccw(a[0], a[1], b[0])*ccw(a[0], a[1], b[1]) <= 0 and ccw(b[0], b[1], a[0])*ccw(b[0], b[1], a[1]) <= 0:
        if ccw(a[0], a[1], b[0])*ccw(a[0], a[1], b[1]) == 0 and ccw(b[0], b[1], a[0])*ccw(b[0], b[1], a[1]) == 0:
            if (max(a[0][0], a[1][0]) >= min(b[0][0], b[1][0]) and max(b[0][0], b[1][0]) >= min(a[0][0], a[1][0])) and (
                max(a[0][1], a[1][1]) >= min(b[0][1], b[1][1]) and max(b[0][1], b[1][1]) >= min(a[0][1], a[1][1])):
                return True
        else:
            return True
    return False

N = int(input())
temp, line = [], []
parent = [i for i in range(N)]
for i in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    temp.append(([x1, y1], [x2, y2]))
    for j in range(i):
        if checkLine(temp[i], temp[j]):
            line.append([i, j])

for i, j in line:
    union(i, j)

result = defaultdict(int)
for i in range(N):
    result[find(i)] += 1
print(len(result.keys()))
print(max(result.values()))