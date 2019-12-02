# Runtime: 120 ms, faster than 81.14% of Python3 online submissions for 3Sum Closest.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for 3Sum Closest.

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()

        dif = float('inf')
        for i in range(len(nums) - 2):
            j,k = i + 1,len(nums) - 1
            while j < k:
                res = nums[i] + nums[j] + nums[k]

                if res == target:
                    return res

                if abs(res - target) < dif:
                    dif = abs(res - target)
                    ans = res

                if res > target:
                    k -= 1

                else:
                    j += 1
        return ans
