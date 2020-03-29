# Runtime: 488 ms, faster than 72.50% of Python3 online submissions for Koko Eating Bananas.
# Memory Usage: 14.3 MB, less than 33.33% of Python3 online submissions for Koko Eating Bananas.

class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:

        l, r = 1, max(piles)
        ans = float("inf")
        while l <= r:
            c = 0
            m = l + (r - l) // 2
            for p in piles:

                c += p // m + 1 if p % m else p // m

            if c <= H:
                if m < ans:
                    ans = m
                r = m - 1

            else:
                l = m + 1
        return ans
