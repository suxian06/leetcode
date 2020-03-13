# Runtime: 24 ms, faster than 95.68% of Python3 online submissions for Play with Chips.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Play with Chips.
class Solution:
    def minCostToMoveChips(self, chips: List[int]) -> int:
        even, odd = 0, 0
        for var in chips:
            if var % 2:
                odd += 1
            else:
                even += 1
        return min(even,odd)
