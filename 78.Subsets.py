class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        for i in range(len(nums), 0, -1):
            res += self.subset(nums,i,i,[])

        return res

    def subset(self,nums, L, iterate ,path):
        res = []
        if len(path) == L:
            return [path]

        else:
            for i in range(len(nums) - iterate + 1):
                res += self.subset(nums[i + 1:], L, iterate - 1,path + [nums[i]])
        return res

            
