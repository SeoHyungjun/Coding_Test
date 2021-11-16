import sys
import math

X, Y = map(int, sys.stdin.readline().split())

print(math.ceil(Y / (Y-X)))