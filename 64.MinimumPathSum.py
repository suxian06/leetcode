# Runtime: 100 ms, faster than 97.46% of Python3 online submissions for Minimum Path Sum.
# Memory Usage: 14.5 MB, less than 70.18% of Python3 online submissions for Minimum Path Sum.

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        dp = [[0 for i in range(n)] for j in range(m)]
        dp[0][0] = grid[0][0]
        for j in range(n - 1):
            dp[0][j + 1] = dp[0][j] + grid[0][j + 1]
        for i in range(m - 1):
            dp[i + 1][0] = dp[i][0] + grid[i + 1][0]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        return dp[-1][-1]
