class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        return self.permut(nums)

    def permut(self,nums):

        if len(nums) == 1:
            return [nums]

        res = []
        for i in range(len(nums)):
            res += [[nums[i]] + x for x in self.permut(nums[:i] + nums[i + 1:])]

        return res
