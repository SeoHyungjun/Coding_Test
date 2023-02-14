import sys

K = int(sys.stdin.readline())
N = int(sys.stdin.readline())
time = 0
for _ in range(N):
    t, z = sys.stdin.readline().split()
    t = int(t)
    time += t
    if time >= 210:
        print(K)
        break
    if z == 'T':
        K = (K + 1) % 9
        if K == 0:
            K += 1