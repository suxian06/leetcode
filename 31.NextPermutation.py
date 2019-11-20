# Runtime: 44 ms, faster than 85.79% of Python3 online submissions for Next Permutation.
# Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Next Permutation.

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 1
        rev = False
        mark = None
        while 0 < i < len(nums):

            if rev == True:
                while nums[mark] < nums[i]:
                    i += 1
                    if i > len(nums) - 1:
                        break
                nums[mark],nums[i - 1] = nums[i - 1],nums[mark]
                nums[mark + 1:] = sorted(nums[mark + 1:])
                break

            elif nums[i] <= nums[i - 1]:
                i -= 1
            else:
                mark = i - 1
                rev = True

        if not rev:
            nums.sort()
