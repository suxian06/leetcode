# Runtime: 120 ms, faster than 99.63% of Python3 online submissions for Container With Most Water.
# Memory Usage: 14.5 MB, less than 38.95% of Python3 online submissions for Container With Most Water.

class Solution:
    def maxArea(self, height: List[int]) -> int:
        square = 0
        i,j = 0, len(height) - 1
        while i < j :
            score = (j - i)*min(height[i],height[j])
            if score > square:
                square = score
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return square
