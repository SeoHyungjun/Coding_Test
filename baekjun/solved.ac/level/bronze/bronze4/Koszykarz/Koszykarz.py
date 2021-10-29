import sys
import math

k, w, m = map(int, sys.stdin.readline().split())

print(math.ceil((w - k) / m))