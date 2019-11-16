# Runtime: 32 ms, faster than 99.79% of Python3 online submissions for Minimum Cost For Tickets.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Minimum Cost For Tickets.
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:

        daysets = set(days)
        dp = [0 for i in range(days[-1] + 1)]
        c1, c2, c3 = 2**31, 2**31, 2**31
        for i in range(days[-1] + 1):
            if i in daysets:
                c1 = max(dp[i - 1],0) + costs[0]
                if i > 7:
                    c2 = dp[i - 7] + costs[1]
                else:
                    c2 = costs[1]
                if i > 30:
                    c3 = dp[i - 30] + costs[2]
                else:
                    c3 = costs[2]
                dp[i] += min(c1,c2,c3)
            else:
                dp[i] = dp[i - 1]

        return dp[-1]
