# Runtime: 24 ms, faster than 96.68% of Python3 online submissions for House Robber II.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for House Robber II.

class Solution:
    def rob(self, nums: List[int]) -> int:
        L = len(nums)
        if L == 0:
            return 0

        if L == 1:
            return nums[0]
        dp1, dp2 = [0]*L, [0]*L
        dp1[0],dp1[1] = nums[0],nums[0]
        dp2[0],dp2[1] = 0,nums[1]
        for i in range(2,L):
            if i == L - 1:
                dp1[i] = dp1[i - 1]
            else:
                dp1[i] = max(dp1[i - 1], dp1[i - 2] + nums[i])
            dp2[i] = max(dp2[i - 1], dp2[i - 2] + nums[i])
            
        return max(dp1[-1],dp2[-1])
