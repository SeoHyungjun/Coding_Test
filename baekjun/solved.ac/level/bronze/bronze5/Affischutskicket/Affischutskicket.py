import sys

a, b, c = map(int, sys.stdin.readline().split())

a *= 0.229*0.324
b *= 0.297*0.420
c *= 0.210*0.297

print(2*a+2*b+c)