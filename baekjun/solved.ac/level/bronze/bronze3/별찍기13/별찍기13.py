import sys

N = int(sys.stdin.readline())
for i in range(N):
    print('*'*(i+1))
for i in range(N-2, -1, -1):
    print('*'*(i+1))