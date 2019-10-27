# Runtime: 80 ms, faster than 92.78% of Python3 online submissions for Max Increase to Keep City Skyline.
# Memory Usage: 14 MB, less than 5.00% of Python3 online submissions for Max Increase to Keep City Skyline.
class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        m, n = len(grid),len(grid[0])
        rowMax = []
        colMax = []
        for i in range(m):
            rowMax.append(max(grid[i]))
        for j in range(n):
            colMax.append(max([grid[i][j] for i in range(m)]))

        count = 0
        for i in range(m):
            for j in range(n):
                count += min(rowMax[i],colMax[j]) - grid[i][j]

        return count
