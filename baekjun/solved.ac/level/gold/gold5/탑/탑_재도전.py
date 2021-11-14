import sys
input = sys.stdin.readline

n = int(input())
tops = list(map(int, input().split()))

answer = []
stack = []

for i in range(n):
    while stack:
        if stack[-1][0] < tops[i]:
            stack.pop()
        else:
            answer.append(stack[-1][1])
            stack.append((tops[i], i+1))
            break
    
    if not stack:
        answer.append(0)
        stack.append((tops[i], i+1))
        continue

print(*answer)