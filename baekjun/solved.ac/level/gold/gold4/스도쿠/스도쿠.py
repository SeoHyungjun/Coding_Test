import sys

def dfs(depth):
    if depth == length:
        for i in range(9):
            print(*board[i])
        exit(0)

    r, c = check[depth]
    avail = row[r] | col[c] | square[r//3 * 3 + c//3]
    for n in avail:
        if n not in row[r] or n not in col[c] or n not in square[r//3 * 3 + c//3]:
            continue
        board[r][c] = n
        row[r].remove(n)
        col[c].remove(n)
        square[r//3 * 3 + c//3].remove(n)
        dfs(depth+1)
        row[r].add(n)
        col[c].add(n)
        square[r//3 * 3 + c//3].add(n)
        board[r][c] = 0


board = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]
row = [set(i for i in range(1, 10)) for _ in range(9)]
col = [set(i for i in range(1, 10)) for _ in range(9)]
square = [set(i for i in range(1, 10)) for _ in range(9)]
all_num = set(i for i in range(1, 10))

check = []
for r in range(9):
    for c in range(9):
        if not board[r][c]:
            check.append((r, c))
            continue
        row[r].remove(board[r][c])
        col[c].remove(board[r][c])
        square[r//3 * 3 + c//3].remove(board[r][c])
        
length = len(check)
dfs(0)