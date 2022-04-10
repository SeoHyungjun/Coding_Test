import sys

M = int(sys.stdin.readline())
N = int(sys.stdin.readline())

answer = []
for i in range(M, N+1):
    if i % (i**0.5) == 0:
        answer.append(i)

if not answer:
    print(-1)
else:
    print(sum(answer))
    print(min(answer))