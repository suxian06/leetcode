# Runtime: 152 ms, faster than 86.79% of Python3 online submissions for Missing Number.
# Memory Usage: 15.9 MB, less than 6.45% of Python3 online submissions for Missing Number.

class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        return list(set(range(len(nums) + 1)).difference(set(nums)))[0]
