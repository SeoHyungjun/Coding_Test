import sys
import math

def get_gcd(a, b):
    while b:
        a, b = b, a%b
    return a

def check_distance(x, y):
    return math.sqrt((x - xs)**2 + (y - ys)**2)

xs, ys = map(int, sys.stdin.readline().split())
xe, ye, dx, dy = map(int, sys.stdin.readline().split())

d_gcd = get_gcd(dx, dy)
dx, dy = dx//d_gcd, dy//d_gcd

curx, cury = xe, ye
while check_distance(curx, cury) > check_distance(curx + dx, cury + dy):
    curx += dx
    cury += dy

print(curx, cury)