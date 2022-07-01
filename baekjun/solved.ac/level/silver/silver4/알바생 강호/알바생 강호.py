import sys

N = int(sys.stdin.readline())
arr = [int(sys.stdin.readline()) for _ in range(N)]
arr.sort(reverse=True)

answer = 0
for i in range(N):
    if arr[i] <= i:
        break
    answer += arr[i] - i

print(answer)