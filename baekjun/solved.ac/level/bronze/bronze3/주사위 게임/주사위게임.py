import sys

N = int(sys.stdin.readline())
answer = 0
for _ in range(N):
    a, b, c = map(int, sys.stdin.readline().split())
    
    if a == b and b == c:
        answer = max(answer, 10000 + a*1000)
    elif a == b or b == c or c == a:
        if a == b:
            answer = max(answer, 1000 + a*100)
        elif b == c:
            answer = max(answer, 1000 + b*100)
        else:
            answer = max(answer, 1000 + c*100)
    else:
        answer = max(answer, max(a, b, c)*100)

print(answer)