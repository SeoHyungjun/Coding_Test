# TLE

class Solution:
    def maxPoints(self, points): #: List[List[int]]) -> int:
        col = len(points)
        row = len(points[0])

        dp = [[0] * row for _ in range(col)]
        dp[0] = points[0]

        for i in range(1, col):
            for j in range(row):
                for k in range(row):
                    dp[i][j] = max(dp[i][j], points[i][j] + dp[i-1][k] - abs(j-k))

        return max(dp[-1])

print(Solution().maxPoints([[1,2,3],[1,5,1],[3,1,1]]))
print(Solution().maxPoints([[1,5],[2,3],[4,2]]))