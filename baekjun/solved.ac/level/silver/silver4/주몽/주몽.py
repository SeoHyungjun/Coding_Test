import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

check = set()
answer = 0
for cur in arr:
    if M - cur in check:
        answer += 1
        check.remove(M - cur)
    else:
        check.add(cur)
        
print(answer)