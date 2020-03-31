# Runtime: 88 ms, faster than 55.62% of Python3 online submissions for Best Time to Buy and Sell Stock III.
# Memory Usage: 13.9 MB, less than 72.73% of Python3 online submissions for Best Time to Buy and Sell Stock III.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        L = len(prices)
        if L == 0:
            return 0

        first = [0 for i in range(L)]
        second = [0 for i in range(L)]
        prev = prices[0]
        for i in range(1,L):
            first[i] = max(0,prices[i] - min(prices[i - 1],prev))
            if prices[i - 1] < prev:
                prev = prices[i - 1]

        profit, prev ,s = 0, prices[L - 1], 0
        for i in range(L - 1, 0, -1):
            if prices[i] > prev:
                prev = prices[i]
            second[i - 1] = max(0,prev - prices[i - 1])
            s = max(second[i],s)
            profit = max(profit,first[i - 1] + s)

        return max(profit,first[-1])
