import sys

N, M = map(int, sys.stdin.readline().split())
S = set(list(map(int, sys.stdin.readline().split()))) if M > 0 else set()

answer = float('inf')
for i in range(1, 1002):
    if i in S: continue
    for j in range(i, 1002):
        if j in S: continue
        for k in range(j, 1002):
            if k in S: continue
            answer = min(answer, abs(N - i*j*k))
    
            if i*j*k >= N:
                break

print(answer)