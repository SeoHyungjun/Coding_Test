import sys

T = int(sys.stdin.readline())
teas = list(map(int, sys.stdin.readline().split()))

print(teas.count(T))