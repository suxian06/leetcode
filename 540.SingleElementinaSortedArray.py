class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:

        i, L = 0, len(nums)
        while i + 1 < L:
            if nums[i] == nums[i + 1]:
                i += 2
            else:
                return nums[i]

        return nums[i]
