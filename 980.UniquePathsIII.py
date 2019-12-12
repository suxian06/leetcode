# Runtime: 48 ms, faster than 97.67% of Python3 online submissions for Unique Paths III.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Unique Paths III.
class Solution:
    c = 0
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        self.c = 0
        m, n = len(grid), len(grid[0])
        total = sum(x.count(0) for x in grid)
        def traverse(pos,total):

            if pos[0] - 1 > -1:
                if grid[pos[0] - 1][pos[1]] == 2:
                    if total == 0:
                        self.c += 1
                        return

                elif grid[pos[0] - 1][pos[1]] == 0:
                    grid[pos[0] - 1][pos[1]] = -1
                    traverse([pos[0] - 1,pos[1]],total - 1)
                    grid[pos[0] - 1][pos[1]] = 0

            if pos[0] + 1 < m:
                if grid[pos[0] + 1][pos[1]] == 2:
                    if total == 0:
                        self.c += 1
                        return
                elif grid[pos[0] + 1][pos[1]] == 0:
                    grid[pos[0] + 1][pos[1]] = -1
                    traverse([pos[0] + 1,pos[1]],total - 1)
                    grid[pos[0] + 1][pos[1]] = 0

            if pos[1] - 1 > -1:
                if grid[pos[0]][pos[1] - 1] == 2:
                    if total == 0:
                        self.c += 1
                        return
                elif grid[pos[0]][pos[1] - 1] == 0:
                    grid[pos[0]][pos[1] - 1] = -1
                    traverse([pos[0],pos[1] - 1],total - 1)
                    grid[pos[0]][pos[1] - 1] = 0

            if pos[1] + 1 < n:
                if grid[pos[0]][pos[1] + 1] == 2:
                    if total == 0:
                        self.c += 1
                        return
                elif grid[pos[0]][pos[1] + 1] == 0:
                    grid[pos[0]][pos[1] + 1] = -1
                    traverse([pos[0],pos[1] + 1],total - 1)
                    grid[pos[0]][pos[1] + 1] = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    traverse([i,j],total)
                    break

        return self.c
