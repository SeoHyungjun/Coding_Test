import sys

N = int(sys.stdin.readline())

for i in range(N):
    print(' '*(N-i-1) + '*'*(i+1))
for i in range(N-2, -1, -1):
    print(' '*(N-i-1) + '*'*(i+1))