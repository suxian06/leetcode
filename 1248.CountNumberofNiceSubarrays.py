# Runtime: 848 ms, faster than 91.56% of Python3 online submissions for Count Number of Nice Subarrays.
# Memory Usage: 20.9 MB, less than 100.00% of Python3 online submissions for Count Number of Nice Subarrays.
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:

        oddPos = [i for i,x in enumerate(nums) if x % 2]
        if len(oddPos) < k:
            return 0
        ans, prev = 0, 0
        for i in range(len(oddPos) - k + 1):

            if i + k < len(oddPos):
                ans += (oddPos[i] + 1 - prev)*(oddPos[i + k] - oddPos[i + k - 1])
                prev = oddPos[i] + 1
            else:
                ans += (oddPos[i] + 1 - prev)*(len(nums) - oddPos[i + k - 1])
                prev = oddPos[i] + 1
        return ans
