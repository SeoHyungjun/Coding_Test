import sys
import math

def ccw(a, b, c, d, e, f):
    return (c - a) * (f - b) - (e - a) * (d - b)

def angle(tri):
    if tri[2] == math.sqrt(tri[0]**2 + tri[1]**2):
        return 'Jikkak'
    if tri[2] < math.sqrt(tri[0]**2 + tri[1]**2):
        return 'Yeahkak'
    return 'Dunkak'

def isosceles(tri):
    if tri[0] == tri[1] or tri[1] == tri[2] or tri[2] == tri[0]:
        return '2'
    return ''

def solve():
    a, b = map(int, sys.stdin.readline().split())
    c, d = map(int, sys.stdin.readline().split())
    e, f = map(int, sys.stdin.readline().split())

    if not ccw(a, b, c, d, e, f):
        return 'X'

    triangle = sorted([math.sqrt((a-c)**2 + (b-d)**2), math.sqrt((c-e)**2 + (d-f)**2), math.sqrt((e-a)**2 + (f-b)**2)])

    if triangle[0] == triangle[2]:
        return 'JungTriangle'
    return angle(triangle) + isosceles(triangle) + 'Triangle'

print(solve())