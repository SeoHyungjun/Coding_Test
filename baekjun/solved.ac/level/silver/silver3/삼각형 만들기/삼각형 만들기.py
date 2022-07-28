import sys

N = int(sys.stdin.readline())
arr = [int(sys.stdin.readline()) for _ in range(N)]
arr.sort(reverse=True)

answer = -1
for i in range(N-2):
    if arr[i] >= arr[i+1] + arr[i+2]:
        continue
    answer = arr[i] + arr[i+1] + arr[i+2]
    break

print(answer)