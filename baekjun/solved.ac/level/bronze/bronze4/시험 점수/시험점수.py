import sys

mingook = list(map(int, sys.stdin.readline().split()))
manse = list(map(int, sys.stdin.readline().split()))

print(max(sum(mingook), sum(manse)))