import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
answer = M
for i in range(N):
    a, b = map(int, sys.stdin.readline().split())
    M += a - b
    if M < 0:
        answer = 0
        break
    answer = max(answer, M)
    
print(answer)