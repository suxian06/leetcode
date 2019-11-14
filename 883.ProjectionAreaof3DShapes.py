# Runtime: 76 ms, faster than 96.99% of Python3 online submissions for Projection Area of 3D Shapes.
# Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Projection Area of 3D Shapes.
class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        res = 0
        maxRow = 0
        for row in grid:
            for x in row:
                if x != 0:
                    res += 1
                if x > maxRow:
                    maxRow = x
            res += maxRow
            maxRow = 0

        grid_m = [*zip(*grid)]
        for row in grid_m:
            res += max(row)
        return res
