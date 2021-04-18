import sys

N = int(sys.stdin.readline())
rgb = [ list(map(int, sys.stdin.readline().split())) for _ in range(N) ]

for i in range(1, N):
    rgb[i][0] = rgb[i][0] + min(rgb[i-1][1], rgb[i-1][2])
    rgb[i][1] = rgb[i][1] + min(rgb[i-1][0], rgb[i-1][2])
    rgb[i][2] = rgb[i][2] + min(rgb[i-1][0], rgb[i-1][1])

print(min(rgb[N-1]))