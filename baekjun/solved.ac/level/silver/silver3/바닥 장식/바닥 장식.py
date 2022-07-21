import sys

N, M = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().rstrip()) for _ in range(N)]

answer = 0
for i in range(N):
    for cur in ''.join(board[i]).split('|'):
        if cur == '':
            continue
        answer += 1

for i in zip(*board):
    for cur in ''.join(i).split('-'):
        if cur == '':
            continue
        answer += 1
        
print(answer)