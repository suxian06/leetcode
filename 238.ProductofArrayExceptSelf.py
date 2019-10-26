class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        L,R,res = [0]*len(nums), [0]*len(nums), [0]*len(nums)
        L[0], R[-1] = 1, 1

        for i in range(1,len(nums)):
            L[i] = L[i - 1]*nums[i - 1]

        for i in range(len(nums) - 2, -1, -1):
            R[i] = R[i + 1]*nums[i + 1]

        for i in range(len(nums)):
            res[i] = R[i] * L[i]

        return res
