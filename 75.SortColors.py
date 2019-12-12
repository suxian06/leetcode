# Runtime: 32 ms, faster than 85.34% of Python3 online submissions for Sort Colors.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Sort Colors.
# two pass
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = {0:0,1:0,2:0}
        for v in nums:
            counts[v] += 1
        for i in range(len(nums)):
            if i < counts[0]:
                nums[i] = 0
            elif i < counts[1] + counts[0]:
                nums[i] = 1
            else:
                nums[i] = 2
# one pass, parition (dutch flag problem)
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p1, p2 = 0, len(nums) - 1
        p = 0
        while p <= p2:
            if nums[p] < 1:
                nums[p], nums[p1] = nums[p1], nums[p]
                p1 += 1
                p += 1
            elif nums[p] > 1:
                nums[p], nums[p2] = nums[p2], nums[p]
                p2 -= 1
            else:
                p += 1
