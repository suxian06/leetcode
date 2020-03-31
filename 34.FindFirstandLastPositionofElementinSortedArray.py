# Runtime: 80 ms, faster than 98.85% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.
# Memory Usage: 14.2 MB, less than 5.36% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        res = [-1,-1]
        l,r = 0, len(nums)

        while l < r:
            m = (l + r) // 2
            if nums[m] == target:
                w = m
                while w > -1 and nums[w] == target:
                    w -= 1
                res[0] = w + 1
                #print(w)
                while m < r and nums[m] == target:
                    m += 1
                res[1] = m - 1
                #print(m)
                break

            elif nums[m] > target:
                r = m

            else:
                l = m + 1
        return res
