import sys

N = int(sys.stdin.readline())

tri = []

for _ in range(N):
    tri.append([0] + list(map(int, sys.stdin.readline().split())) + [0])

for i in range(1,N):
    for j in range(1,len(tri[i])-1):
        tri[i][j] += max(tri[i-1][j], tri[i-1][j-1])

print(max(tri[N-1]))