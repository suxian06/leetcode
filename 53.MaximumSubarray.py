class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        curNum = 0
        curMin = 0
        res = -100000

        if len(nums) == 1:
            return nums[0]

        for i in range(len(nums)):
            curNum += nums[i]

            if curNum - curMin > res:
                res = curNum - curMin

            if curNum < curMin:
                curMin = curNum

        return res
