# Runtime: 44 ms, faster than 95.09% of Python3 online submissions for Find Peak Element.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Find Peak Element.

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l,h = 0, len(nums) - 1
        while l < h:
            m = (l + h) // 2
            if nums[m] < nums[m + 1]:
                l = m + 1
            else:
                h = m
        return l
