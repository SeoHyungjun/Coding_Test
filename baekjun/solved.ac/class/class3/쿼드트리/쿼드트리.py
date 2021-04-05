import sys

board = []

def all_equal(x, y, size):
    tmp =board[x][y]
    for i in range(size):
        for j in range(size):
            if board[x + i][y + j] != tmp:
                return False
    return True

def check(x, y, size):
    if all_equal(x, y, size):
        return board[x][y]
    else:
        answer = ''
        for i in range(2):
            for j in range(2):
                answer += check(x + i*size//2, y + j*size//2, size//2)
        return '(' + answer + ')'

n = int(sys.stdin.readline())

for _ in range(n):
    board.append(list(sys.stdin.readline().rstrip('\n')))

print(check(0, 0, n))