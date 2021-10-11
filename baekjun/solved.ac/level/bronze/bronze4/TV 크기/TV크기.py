import sys
import math

D, H, W = map(int, sys.stdin.readline().split())
x = math.sqrt(D**2 / (H**2 + W**2))
print(math.floor(H*x), math.floor(W*x))