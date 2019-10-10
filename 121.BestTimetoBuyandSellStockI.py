class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0

        L = len(prices)

        if L < 2:
            return 0

        cur_val = L - 1
        next_val = L - 2

        while next_val > -1:

            if prices[cur_val] - prices[next_val] > profit:
                profit = prices[cur_val] - prices[next_val]

            elif prices[cur_val] < prices[next_val]:
                cur_val  = next_val

            next_val -= 1

        return profit

        
