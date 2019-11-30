# Runtime: 44 ms, faster than 98.46% of Python3 online submissions for Search Insert Position.
# Memory Usage: 13.5 MB, less than 100.00% of Python3 online submissions for Search Insert Position.

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        def bsearch(nums,l,h,target):

            while l < h:
                m = (l + h) // 2
                if nums[m] == target:
                    return m

                elif nums[m] > target:
                    h = m

                else:
                    l = m + 1

            if nums[l - 1] < target < nums[l]:
                return l

        if not nums:
            return 0

        if target > nums[-1]:
            return len(nums)

        if target < nums[0]:
            return 0

        return bsearch(nums,0,len(nums),target)
