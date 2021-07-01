import sys

N = int(sys.stdin.readline())

board, black, white = [], [], []
avail_rightdown = [True] * (2*N-1)
avail_leftdown = [True] * (2*N-1)
sum_b_w = [0, 0]

for i in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))
    for j in range(N):
        if board[i][j]:
            if (i+j) % 2 == 0:
                black.append((i, j))
            else:
                white.append((i, j))

def dfs(avail, used, index):
    if not avail:
        global sum_b_w
        sum_b_w[index] = max(sum_b_w[index], len(used))
        return

    x, y = avail.pop()
    # x,y 에 안 놓을 경우
    dfs(avail, used, index)
    # x,y 에 놓을 경우
    rd = x-y+N-1
    ld = x+y
    if avail_rightdown[rd] and avail_leftdown[ld]:
        avail_rightdown[rd] = False
        avail_leftdown[ld] = False
        used.append((x, y))
        dfs(avail, used, index)
        used.pop()
        avail_rightdown[rd] = True
        avail_leftdown[ld] = True

    avail.append((x, y))

if black:
    used = []
    dfs(black, used, 0)
if white:
    used = []
    dfs(white, used, 1)

print(sum(sum_b_w))
