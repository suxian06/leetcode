class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = len(nums)
        i = 0
        while count > 0:
            if nums[i] == 0:
                nums.append(nums.pop(i))
            else:
                i += 1

            count -= 1
        
