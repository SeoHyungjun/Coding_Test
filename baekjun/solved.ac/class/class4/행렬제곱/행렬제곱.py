import sys

def multi(board1, board2):
    len_board = len(board1)
    new_board = [[0]*len_board for _ in range(len_board)]

    for i in range(len_board):
        for j in range(len_board):
            for k in range(len_board):
                new_board[i][j] += (board1[i][k] * board2[k][j] % 1000)

    return new_board

def matrix(board, B):
    if B == 1:
        return board

    if B % 2 == 0:
        mul = matrix(board, B//2)
        return multi(mul, mul)

    else:
        mul = matrix(board, (B-1)//2)
        return multi(multi(mul, mul), board)

def solve():
    N, B = map(int, sys.stdin.readline().split())
    board = []

    for _ in range(N):
        board.append([i%1000 for i in map(int, sys.stdin.readline().split())])

    board = matrix(board, B)

    for i in range(N):
        for j in range(N):
            print(board[i][j]%1000, end = ' ')
        print()

solve()