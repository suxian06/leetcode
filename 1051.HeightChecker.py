# Runtime: 20 ms, faster than 82.42% of Python online submissions for Height Checker.
# Memory Usage: 11.8 MB, less than 100.00% of Python online submissions for Height Checker.
class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        pos = sorted(heights)
        return sum(x != y for x,y in zip(pos,heights))
