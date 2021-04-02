import sys
input = sys.stdin.readline

n = int(input())

board = [ list(map(int, input().split())) for _ in range(n)]
dic = {0:0, 1:0}

def all_same(x, y, size):
    tmp = board[x][y]

    for i in range(size):
        for j in range(size):
            if board[x+i][y+j] != tmp:
                return False

    return True

def solve(x, y, size):
    if all_same(x, y, size):
        dic[board[x][y]] += 1
        return
    
    for i in range(2):
        for j in range(2):
            solve(x + (i * size//2), y + (j * size//2), size//2)


solve(0, 0, n)
print(dic[0])
print(dic[1])