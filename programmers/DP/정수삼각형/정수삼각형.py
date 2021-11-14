def solution(triangle):
    dp = [[0]*i for i in range(1, len(triangle)+1)]
    dp[0][0] = triangle[0][0]

    for i in range(len(triangle)-1):
        for j in range(len(triangle[i])):
            for k in range(2):
                if dp[i+1][j+k] == 0:
                    dp[i+1][j+k] = dp[i][j] + triangle[i+1][j+k]
                else:
                    dp[i+1][j+k] = max(dp[i+1][j+k], dp[i][j] + triangle[i+1][j+k])

    return max(dp[-1])


print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))