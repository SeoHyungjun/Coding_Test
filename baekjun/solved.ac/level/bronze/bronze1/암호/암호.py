import sys

K = int(sys.stdin.readline())
prev = sys.stdin.readline().rstrip()

board = []
for i in range(len(prev)//K):
    board.append(list(prev[K*i:K*i+K]) if not i%2 else list(prev[K*i:K*i+K])[::-1])

answer = ''
for j in range(K):
    for i in range(len(prev)//K):
        answer += board[i][j]

print(answer)