import sys
import math

N, A, B, C, D = map(int, sys.stdin.readline().split())

print(min(math.ceil(N/A)*B, math.ceil(N/C)*D))