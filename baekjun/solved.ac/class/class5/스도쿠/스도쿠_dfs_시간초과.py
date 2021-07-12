import sys
from copy import deepcopy

def compare(arr, answer):
    for i in range(9):
        for j in range(9):
            if arr[i][j] < answer[i][j]:
                return True
            elif arr[i][j] > answer[i][j]:
                return False
    return False

def insqure(x, y, val, arr):
    a, _ = divmod(x, 3)
    b, _ = divmod(y, 3)

    for i in range(3):
        for j in range(3):
            if arr[a*3+i][b*3+j] == val:
                return False
    return True


def dfs(stack, arr, answer):
    if not stack:
        if compare(arr, answer):
            for i in range(9):
                answer[i] = arr[i][:]
        return

    x, y = stack.pop()
    for i in range(1, 10):
        if insqure(x, y, i, arr):
            check = True
            for j in range(9):
                if arr[x][j] == i or arr[j][y] == i:
                    check = False
                    break

            if check:
                arr[x][y] = i
                dfs(stack, arr, answer)
                arr[x][y] = 0

    stack.append((x, y))

arr = [list(map(int, list(sys.stdin.readline().strip()))) for _ in range(9)]
answer = [[10]*9 for _ in range(9)]

stack = []
for i in range(9):
    for j in range(9):
        if arr[i][j] == 0:
            stack.append((i, j))

dfs(stack, arr, answer)
for i in range(9):
    print(*answer[i], sep = '')