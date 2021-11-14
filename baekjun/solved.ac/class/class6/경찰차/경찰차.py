import sys
sys.setrecursionlimit(10**9)

def dist(a, b): # a -> b 갈때의 거리
    return abs(acident[a][0] - acident[b][0]) + abs(acident[a][1] - acident[b][1])


def solve(x, y): # acident 배열에서 police1,2의 위치 x,y
    global dp

    next_index = max(x, y) + 1
    if next_index >= M + 2:
        return 0

    if dp[x][y] == -1:
        dp[x][y] = min(solve(next_index, y) + dist(x, next_index), solve(x, next_index) + dist(y, next_index))

    return dp[x][y]


def find_path(x, y):
    next_index = max(x, y) + 1
    if next_index >= M + 2:
        return
    
    move_x = dp[next_index][y] + dist(x, next_index)
    move_y = dp[x][next_index] + dist(y, next_index)

    if move_x <= move_y:
        print(1)
        find_path(next_index, y)
    else:
        print(2)
        find_path(x, next_index)


N = int(sys.stdin.readline())
police1 = [1, 1]
police2 = [N, N]

M = int(sys.stdin.readline())
acident = [[1, 1], [N, N]] + [list(map(int, sys.stdin.readline().split())) for _ in range(M)]

dp = [[-1] * (M+2) for _ in range(M+2)]
print(solve(0, 1))
find_path(0, 1)