import sys

def check(x, y):
    arr = []
    for i in range(x, x + 3):
        for j in range(y, y + 3):
            arr.append(board[i][j])
    arr.sort()

    return arr[4]

R, C = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(R)]
T = int(sys.stdin.readline())

J = []
answer = 0
for i in range(R - 2):
    for j in range(C - 2):
        J.append(check(i, j))

print(len([j for j in J if j >= T ]))