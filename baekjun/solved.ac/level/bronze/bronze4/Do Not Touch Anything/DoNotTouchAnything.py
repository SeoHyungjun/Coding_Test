import sys
import math

R, C, N = map(int, sys.stdin.readline().split())
print(math.ceil(R/N) * math.ceil(C/N))