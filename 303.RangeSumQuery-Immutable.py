# Runtime: 84 ms, faster than 96.28% of Python3 online submissions for Range Sum Query - Immutable.
# Memory Usage: 16.4 MB, less than 100.00% of Python3 online submissions for Range Sum Query - Immutable.

class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.L = len(nums)
        self.dp = [0 for i in range(self.L + 1)]

        for i in range(self.L):
            self.dp[i + 1] = self.dp[i] + nums[i]
        #print(self.dp)
    def sumRange(self, i: int, j: int) -> int:

        return self.dp[j + 1] - self.dp[i]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
