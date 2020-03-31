# Runtime: 1196 ms, faster than 33.97% of Python3 online submissions for Longest Increasing Subsequence.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Longest Increasing Subsequence.
# n^2 solution
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        L = len(nums)
        if L < 2:
            return L
        maxLength = 0
        length = [1]*L
        for i in range(1,L):
            for j in range(i):
                if nums[i] > nums[j]:
                    length[i] = max(length[j] + 1, length[i])
            if length[i] > maxLength:
                maxLength = length[i]

        return maxLength

# need update with binary search
