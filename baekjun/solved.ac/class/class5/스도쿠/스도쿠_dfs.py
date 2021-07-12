import sys

arr = [list(map(int, list(sys.stdin.readline().strip()))) for _ in range(9)]
zero = [(i, j) for i in range(9) for j in range(9) if arr[i][j] == 0]
state = False

def avail(x, y):
    not_used = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    for i in range(9):
        if arr[i][y] in not_used:
            not_used.remove(arr[i][y])

        if arr[x][i] in not_used:
            not_used.remove(arr[x][i])

    x, y = x // 3 * 3, y // 3 * 3
    for i in range(3):
        for j in range(3):
            if arr[x + i][y + j] in not_used:
                not_used.remove(arr[x + i][y + j])
                
    return not_used

def dfs(index):
    global arr, state
    if state:
        return

    if index >= len(zero):
        for i in arr:
            print(*i, sep='')
        state = True
        return

    x, y = zero[index]
    not_used = avail(x, y)
    for i in not_used:
        arr[x][y] = i
        dfs(index+1)
        arr[x][y] = 0

dfs(0)