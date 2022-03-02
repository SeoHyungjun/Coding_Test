import sys

N, L, D = map(int, sys.stdin.readline().split())
check = [True] * (N*L + 5*(N-1))

for i in range(N):
    start = (L+5) * i

    for j in range(L):
        check[start+j] = False

answer = 0
while len(check) > answer and not check[answer]:
    answer += D

print(answer)