# Runtime: 36 ms, faster than 96.76% of Python3 online submissions for Search in Rotated Sorted Array.
# Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Search in Rotated Sorted Array.
# very annoying edge cases. code looks very messy...
class Solution:
    def search(self, nums: List[int], target: int) -> int:

        if not nums:
            return -1

        i , L = 0, len(nums)
        while i < L - 1 and nums[i] < nums[i + 1]:
            i += 1
        pivot = i

        def bsearch(nums,l,h,target):

            while l < h:
                m = (l + h) // 2
                print(m)
                if nums[m] == target:
                    return m

                elif nums[m] > target:
                    h = m
                else:
                    l = m + 1
            return -1

        if pivot + 1 == L:

            return bsearch(nums,0,L,target)

        if nums[0] <= target <= nums[pivot]:
            if pivot > 0:
                return bsearch(nums[:pivot + 1],0,pivot + 1,target)
            elif nums[pivot] == target:
                return pivot
            else:
                return -1

        elif nums[pivot + 1] <= target <= nums[-1]:
            if pivot + 1 < L - 1:
                v = bsearch(nums[pivot + 1:],0,L - pivot - 1,target)
                if v == -1:
                    return v
                else:
                    return pivot + 1 + v
            elif nums[pivot + 1] == target:
                return pivot + 1
            else:
                return -1
        else:
            return -1
