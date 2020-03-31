# Runtime: 52 ms, faster than 95.10% of Python3 online submissions for Minimum Time Visiting All Points.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Minimum Time Visiting All Points.

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:

        c = 0
        prev = points[0]
        for p in points[1:]:
            x, y = abs(p[0] - prev[0]), abs(p[1] - prev[1])
            c += min(x,y) + abs(x - y)
            prev = p
        return c
