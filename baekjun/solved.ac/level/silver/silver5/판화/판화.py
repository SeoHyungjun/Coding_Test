import sys

direction = {'U':[-1, 0], 'D':[1, 0], 'L':[0, -1], 'R':[0, 1]}
scretchs = {'U':'|', 'D':'|', 'L':'-', 'R':'-'}

def make_scretch(x, y, move):
    global board
    scretch = board[x][y]

    if scretch == '.':
        board[x][y] = scretchs[move]
    elif scretch == '-' and scretchs[move] == '|':
        board[x][y] = '+'
    elif scretch == '|' and scretchs[move] == '-':
        board[x][y] = '+'


def move_in_board(x, y, move):    
    nx, ny = x + direction[move][0], y + direction[move][1]

    if not (0 <= nx < N) or not (0 <= ny < N):
        return x, y

    make_scretch(x, y, move)
    make_scretch(nx, ny, move)

    return nx, ny


N = int(sys.stdin.readline())
board = [['.'] * N for _ in range(N)]

x, y = 0, 0
for move in sys.stdin.readline().rstrip():
    x, y = move_in_board(x, y, move)

for cur in board:
    print(''.join(cur))