import sys

def multi_matrix(a, b):
    new_board = [[0] * 8 for _ in range(8)]
    for i in range(8):
        for j in range(8):
            for k in range(8):
                new_board[i][j] += a[i][k] * b[k][j] % 1000000007

    return new_board

def solve(num):
    if num in dp:
        return dp[num]

    if num % 2 == 0:
        dp[num//2] = solve(num//2)
        return multi_matrix(dp[num//2], dp[num//2])
    else:
        dp[(num-1)//2] = solve((num-1)//2)
        return multi_matrix(multi_matrix(dp[(num-1)//2], dp[(num-1)//2]), dp[1])

board = [[0, 1, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 0, 0, 0, 1],
        [0, 1, 0, 1, 0, 0, 1, 1],
        [0, 0, 1, 0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0, 1, 0, 0],
        [0, 0, 0, 0, 1, 0, 1, 0],
        [0, 0, 1, 1, 0, 1, 0, 1],
        [1, 1, 1, 0, 0, 0, 1, 0]]

D = int(sys.stdin.readline())
dp = {1:board}

print(solve(D)[0][0] % 1000000007)