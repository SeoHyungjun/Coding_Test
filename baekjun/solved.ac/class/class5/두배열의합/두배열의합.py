import sys

T = int(sys.stdin.readline())
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split()))

sum_A = {}
for i in range(N):
    for j in range(i, N):
        tmp = sum(A[i:j+1])
        if tmp not in sum_A:
            sum_A[tmp] = 1
        else:
            sum_A[tmp] += 1

sum_B = {}
for i in range(M):
    for j in range(i, M):
        tmp = sum(B[i:j+1])
        if tmp not in sum_B:
            sum_B[tmp] = 1
        else:
            sum_B[tmp] += 1

answer = 0
for i in sum_A.keys():
    if T - i in sum_B:
        answer += sum_A[i] * sum_B[T-i]

print(answer)