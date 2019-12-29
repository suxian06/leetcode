# Runtime: 364 ms, faster than 90.65% of Python3 online submissions for Find All Numbers Disappeared in an Array.
# Memory Usage: 23.6 MB, less than 7.14% of Python3 online submissions for Find All Numbers Disappeared in an Array.
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        return set(list(range(1,len(nums) + 1))).difference(set(nums))
# Runtime: 372 ms, faster than 83.95% of Python3 online submissions for Find All Numbers Disappeared in an Array.
# Memory Usage: 22.3 MB, less than 7.14% of Python3 online submissions for Find All Numbers Disappeared in an Array.
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        L = len(nums)
        seen = set(list(range(1,L + 1)))
        for i in range(L):
            seen.discard(nums[i])
        return list(seen)
