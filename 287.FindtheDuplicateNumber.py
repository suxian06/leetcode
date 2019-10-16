class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        stack = set()

        for val in nums:

            if val in stack:
                return val

            stack.add(val)
        
