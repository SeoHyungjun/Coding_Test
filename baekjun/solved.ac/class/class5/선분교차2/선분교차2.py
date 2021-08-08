import sys

def ccw(a, b, c):
    return (a[0]*b[1] + b[0]*c[1] + c[0]*a[1]) - (b[0]*a[1] + c[0]*b[1] + a[0]*c[1])

def check(a, b, c, d):
    if ccw(a, b, c)*ccw(a, b, d) <= 0 and ccw(c, d, a)*ccw(c, d, b) <= 0:
        if ccw(a, b, c)*ccw(a, b, d) == 0 and ccw(c, d, a)*ccw(c, d, b) == 0:
            if (max(a[0], b[0]) >= min(c[0], d[0]) and
            max(c[0], d[0]) >= min(a[0], b[0]) and
            max(a[1], b[1]) >= min(c[1], d[1]) and
            max(c[1], d[1]) >= min(a[1], b[1])):
                return 1
        else:
            return 1
    return 0

x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
x3, y3, x4, y4 = map(int, sys.stdin.readline().split())

print(check([x1, y1], [x2, y2], [x3, y3], [x4, y4]))