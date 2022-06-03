import sys

N = int(sys.stdin.readline())
A = sorted(list(map(int, sys.stdin.readline().split())))
B = sorted(list(map(int, sys.stdin.readline().split())), reverse=True)

answer = 0
for i in range(N):
    answer += A[i] * B[i]

print(answer)