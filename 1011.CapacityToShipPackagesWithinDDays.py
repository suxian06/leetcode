# Runtime: 524 ms, faster than 84.86% of Python3 online submissions for Capacity To Ship Packages Within D Days.
# Memory Usage: 15.8 MB, less than 10.00% of Python3 online submissions for Capacity To Ship Packages Within D Days.
class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        l, r = max(weights), sum(weights)
        while l <= r:
            m, d , cur  = l + (r - l)//2, 1, 0

            for w in weights:
                cur += w
                if cur > m:
                    d += 1
                    cur = w

            if d > D:
                l = m + 1
            else:
                r = m - 1
        return l
