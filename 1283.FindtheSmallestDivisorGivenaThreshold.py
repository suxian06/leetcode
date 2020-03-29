# Runtime: 404 ms, faster than 78.79% of Python3 online submissions for Find the Smallest Divisor Given a Threshold.
# Memory Usage: 19.3 MB, less than 100.00% of Python3 online submissions for Find the Smallest Divisor Given a Threshold.
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l, r = 1, max(nums)
        while l <= r:
            m = l + (r - l) // 2
            cur = 0
            for n in nums:
                cur += n // m + 1 if n % m else n // m

            if cur <= threshold:
                r = m - 1

            else:
                l = m + 1
        return l
#
