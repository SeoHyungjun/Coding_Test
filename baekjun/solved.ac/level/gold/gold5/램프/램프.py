import sys

N, M = map(int, sys.stdin.readline().split())
arr = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(N)]
K = int(sys.stdin.readline())
answer = 0

for i in range(N):
    zero = M - sum(arr[i])
    cnt = 0
    if zero <= K and zero%2 == K%2:
        for j in range(N):
            if arr[i] == arr[j]:
                cnt += 1
        answer = max(answer, cnt)

print(answer)