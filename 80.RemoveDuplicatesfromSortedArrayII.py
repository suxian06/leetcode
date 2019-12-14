# Runtime: 52 ms, faster than 93.90% of Python3 online submissions for Remove Duplicates from Sorted Array II.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Remove Duplicates from Sorted Array II.

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        if not nums:
            return 0
        i = 1
        prev, c = nums[0], 1
        while i < len(nums):

            if nums[i] == prev:
                c += 1

            else:
                prev = nums[i]
                c = 1

            if c > 2:
                nums.pop(i)
                c -= 1
                i -= 1
            i += 1


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        count = 0
        for j in range(1, len(nums)):
            if nums[j] == nums[i]:
                count += 1
                if count == 1:
                    i += 1
                    nums[i] = nums[j]
            else:
                count = 0
                i += 1
                nums[i] = nums[j]
        return i + 1
