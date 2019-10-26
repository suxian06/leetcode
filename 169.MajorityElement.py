class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        note = nums[0]
        count = 1

        for val in nums[1:]:
            if count == 0:
                note = val

            if val == note:
                count += 1

            else:
                count -= 1
        return note
