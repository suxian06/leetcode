# Runtime: 36 ms, faster than 90.99% of Python3 online submissions for Best Time to Buy and Sell Stock with Cooldown.
# Memory Usage: 13.1 MB, less than 100.00% of Python3 online submissions for Best Time to Buy and Sell Stock with Cooldown.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if len(prices) < 2:
            return 0
        dp = [ [0]*2 for i in range(len(prices))]
        dp[0][1] = - prices[0]
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i - 1][0],prices[i] + dp[i - 1][1])
            dp[i][1] = max(dp[i - 1][1],dp[i - 2][0] - prices[i])
        return dp[-1][0]
