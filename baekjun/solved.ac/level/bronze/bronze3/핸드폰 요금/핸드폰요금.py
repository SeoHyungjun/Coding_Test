import sys
import math

N = int(sys.stdin.readline())
times = list(map(int, sys.stdin.readline().split()))

Y, M = 0, 0
for time in times:
    Y += math.ceil((time+1)/30) * 10
    M += math.ceil((time+1)/60) * 15

if Y < M:
    print('Y', Y)
elif Y > M:
    print('M', M)
else:
    print('Y M', Y)