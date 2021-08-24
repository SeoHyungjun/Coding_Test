import sys

def check(num):
    if num**0.5 == int(num**0.5):
        return True
    return False

N, M = map(int, sys.stdin.readline().split())
arr = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(N)]
answer = -1

for i in range(N):
    for j in range(M):
        for di in range(-N, N):
            for dj in range(-M, M):
                if di == 0 and dj == 0:
                    continue
                num = ''
                row = i
                col = j

                while 0 <= row < N and 0 <= col < M:
                    num += str(arr[row][col])
                    if check(int(num)):
                        answer = max(answer, int(num))
                    
                    row += di
                    col += dj

print(answer)