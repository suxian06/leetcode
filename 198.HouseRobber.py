class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        prevOne = 0
        prevTwo = 0
        maxSum = 0

        for i in range(len(nums)):
            if i == 0:
                maxSum = nums[0]

            elif i == 1:
                maxSum = max(nums[0],nums[1])

            else:
                maxSum = max(prevTwo + nums[i], prevOne)

            prevTwo = prevOne
            prevOne = maxSum


        return maxSum

        
