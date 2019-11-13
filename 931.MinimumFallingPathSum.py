# Runtime: 108 ms, faster than 99.43% of Python3 online submissions for Minimum Falling Path Sum.
# Memory Usage: 13.2 MB, less than 100.00% of Python3 online submissions for Minimum Falling Path Sum.
class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        L = len(A)
        dp = [[0 for i in range(L)] for j in range(L + 1)]
        dp[1] = A[0]
        for i in range(1, L):
            dp[i + 1][0] = A[i][0] + min(dp[i][0], dp[i][1])
            dp[i + 1][-1] = A[i][-1] + min(dp[i][-1], dp[i][-2])
            for j in range(1, L - 1):
                dp[i + 1][j] = A[i][j] + min(dp[i][j - 1], dp[i][j], dp[i][j + 1])
        
        return min(dp[L])
