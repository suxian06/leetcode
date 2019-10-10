class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        L = len(prices)

        if L < 2:
            return 0

        pre_ele = 0
        cur_ele = 0
        next_ele = 1
        profit = 0

        while next_ele < L:

            if prices[cur_ele] <= prices[next_ele]:
                cur_ele += 1
                next_ele += 1
                if next_ele == L:
                    profit += prices[cur_ele] - prices[pre_ele]

            else:
                profit += prices[cur_ele] - prices[pre_ele]
                pre_ele = next_ele
                next_ele += 1
                cur_ele += 1

        return profit


        
