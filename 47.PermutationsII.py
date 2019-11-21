# Runtime: 56 ms, faster than 92.44% of Python3 online submissions for Permutations II.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Permutations II.
class Solution:
    def permuteUnique(self, nums):
        res = []

        def traverse(nums,path,res):
            seenSet = set()
            for i in range(len(nums)):
                if nums[i] not in seenSet:
                    traverse(nums[:i] + nums[i + 1:], path + [nums[i]], res)
                    seenSet.add(nums[i])
            if not nums:
                res.append(path)
        traverse(nums,[],res)
        return res
