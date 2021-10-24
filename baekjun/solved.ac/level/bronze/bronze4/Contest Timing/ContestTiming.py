import sys

D, H, M = map(int, sys.stdin.readline().split())

answer = (D - 11) * 24*60 + (H - 11) * 60 + M - 11
print(answer if answer >= 0 else -1)