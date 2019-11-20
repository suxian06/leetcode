# Runtime: 40 ms, faster than 98.78% of Python3 online submissions for Unique Paths II.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Unique Paths II.
class Solution:

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m,n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for i in range(n)] for j in range(m)]

        if obstacleGrid[0][0] == 0:
            dp[0][0] = 1
        else:
            return 0

        for i in range(m):
            for j in range(1,n):

                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0

                elif i == 0:
                    dp[i][j] = dp[i][j - 1]

                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

            if i + 1 < m:
                if obstacleGrid[i + 1][0] == 1:
                    dp[i + 1][0] = 0
                else:
                    dp[i + 1][0] = dp[i][0]

        return dp[m - 1][n - 1]
