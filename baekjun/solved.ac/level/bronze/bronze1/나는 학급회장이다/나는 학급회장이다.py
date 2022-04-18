import sys

N = int(sys.stdin.readline())
point = [[1, 0, 0, 0], [2, 0, 0, 0], [3, 0, 0, 0]]

for _ in range(N):
    a, b, c = map(int, sys.stdin.readline().split())
    point[0][a] += 1
    point[1][b] += 1
    point[2][c] += 1

point = sorted(point, key = lambda x: (-(3*x[3] + 2*x[2] + x[1]), -x[3], -x[2]))

if point[0][1:] == point[1][1:]:
    print(0, 3*point[0][3] + 2*point[0][2] + point[0][1])
else:
    print(point[0][0], 3*point[0][3] + 2*point[0][2] + point[0][1])