import sys

K = float(sys.stdin.readline())

D1, D2 = map(float, sys.stdin.readline().split())
D1, D2 = min(D1, D2), max(D1, D2)
H = K**2 - ((D2-D1)/2)**2

print(H)