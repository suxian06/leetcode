# Runtime: 32 ms, faster than 94.37% of Python3 online submissions for Remove Element.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Remove Element.
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        L = len(nums)
        i = 0
        while i < L:
            if nums[i] == val:
                nums[i:] = nums[i + 1:]
            else:
                i += 1
            L = len(nums)

# Runtime: 28 ms, faster than 98.36% of Python3 online submissions for Remove Element.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Remove Element.
# tricky
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while val in set(nums):
            nums.remove(val)
