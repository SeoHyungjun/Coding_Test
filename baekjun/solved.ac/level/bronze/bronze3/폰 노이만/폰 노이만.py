import sys

P = int(sys.stdin.readline())

for _ in range(P):
    N, D, A, B, F = map(float, sys.stdin.readline().split())
    answer = D / (A + B) * F
    print("%d %.6f" % (N, answer))