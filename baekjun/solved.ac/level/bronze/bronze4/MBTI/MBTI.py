import sys

jinho = sys.stdin.readline().rstrip()
N = int(sys.stdin.readline())
answer = 0
for _ in range(N):
    if jinho == sys.stdin.readline().rstrip():
        answer += 1
        
print(answer)