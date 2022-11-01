import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
answer = [-1] * N
stack = []

for i in range(N):
    while stack and arr[stack[-1]] < arr[i]:
        answer[stack.pop()] = arr[i]
    stack.append(i)

print(*answer)