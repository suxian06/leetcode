# Runtime: 52 ms, faster than 73.97% of Python3 online submissions for Search in Rotated Sorted Array II.
# Memory Usage: 13.1 MB, less than 100.00% of Python3 online submissions for Search in Rotated Sorted Array II.
class Solution:
    def search(self, nums: List[int], target: int) -> bool:

        if not nums:
            return False

        if len(nums) == 1 and nums[0] != target:
            return False

        l_index ,h_index = 0, len(nums) - 1

        while l_index <= h_index:
            l, r = nums[l_index], nums[h_index]
            m = (l_index + h_index) // 2

            if nums[m] == target:
                return True

            elif nums[m] < target:
                if r >= target:
                    l_index = m + 1
                else:
                    while nums[h_index - 1] < nums[h_index]:
                        h_index -= 1
                    h_index -= 1

            elif nums[m] > target:
                if l <= target:
                    h_index = m - 1
                else:
                    while l_index + 1 < len(nums) and nums[l_index + 1] > nums[l_index]:
                        l_index += 1
                    l_index += 1

        return False
