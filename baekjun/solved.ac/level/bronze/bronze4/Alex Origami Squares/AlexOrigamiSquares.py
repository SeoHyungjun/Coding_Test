import sys

h, w = map(int, sys.stdin.readline().split())
h, w = max(h, w), min(h, w)

print(max(h/3 if h/3 <= w else w, w/2))