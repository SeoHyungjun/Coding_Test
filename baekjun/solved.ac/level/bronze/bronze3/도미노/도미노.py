import sys

N = int(sys.stdin.readline())
answer = 0

for i in range(N+1):
    for j in range(i+1):
        answer += j + i

print(answer)