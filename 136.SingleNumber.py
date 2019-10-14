class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        table = {}

        for i in range(len(nums)):
            if nums[i] not in table:
                table[nums[i]] = 1
            else:
                table[nums[i]] += 1

        return min(table.keys(), key=table.get)
        
