import sys

def check(line):
    for i in range(1, N):
        diff = line[i-1] - line[i]
        if abs(diff) > 1:
            return False
        if diff > 0:
            for j in range(L):
                if i + j >= N or line[i] != line[i+j] or slope[i+j]:
                    return False
                slope[i+j] = True
        elif diff < 0:
            for j in range(L):
                if i-j-1 < 0 or line[i-1] != line[i-j-1] or slope[i-j-1]:
                    return False
                slope[i-j-1] = True
    
    return True

N, L = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
answer = 0

for i in range(N):
    slope = [False] * N
    if check([board[i][j] for j in range(N)]):
        answer += 1
    slope = [False] * N
    if check([board[j][i] for j in range(N)]):
        answer += 1

print(answer)
