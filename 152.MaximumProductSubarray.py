class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        curNum = 1
        curMaxNeg = -1000000
        curMax = 0
        multMax = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                curNum *= nums[i]

            else:
                curNum = 1
                curMax = max(curMax,multMax)
                curMaxNeg = -1000000
                multMax = 0
                continue

            if curNum > 0 and curNum > curMax:
                curMax = curNum

            if curNum / curMaxNeg > multMax:
                multMax = int(curNum / curMaxNeg)

            if curNum < 0 and curNum > curMaxNeg:
                curMaxNeg = curNum

        return max(multMax, curMax)
            
