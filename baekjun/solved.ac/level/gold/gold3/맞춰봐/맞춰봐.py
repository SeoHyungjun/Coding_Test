import sys

def check(index):
    sum = 0
    for i in range(index, -1, -1):
        sum += answer[i]
        if sum == 0 and S[i][index] != 0:
            return False
        elif sum < 0 and S[i][index] >= 0:
            return False
        elif sum > 0 and S[i][index] <= 0:
            return False

    return True

def solve(index):
    if index == N:
        return True

    if S[index][index] == 0:
        answer[index] = 0
        return solve(index+1)
    
    for i in range(1, 11):
        answer[index] = S[index][index] * i
        if check(index) and solve(index+1):
            return True
    return False

N = int(sys.stdin.readline())
arr = list(sys.stdin.readline())
S = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(i, N):
        temp = arr.pop(0)
        if temp == '+':
            S[i][j] = 1
        elif temp == '-':
            S[i][j] = -1
    
answer = [0]*N
solve(0)
print(*answer)