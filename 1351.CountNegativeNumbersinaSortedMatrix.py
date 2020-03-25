# Runtime: 112 ms, faster than 99.67% of Python3 online submissions for Count Negative Numbers in a Sorted Matrix.
# Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Count Negative Numbers in a Sorted Matrix.

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:

        m,n = len(grid),len(grid[0])
        count = 0
        for i in range(m):
            l,r = 0,n - 1

            if grid[i][0] < 0:
                count += n
                #print(n)
            elif grid[i][n - 1] >= 0:
                continue


            else:

                while l <= r:
                    m = (l + r) // 2

                    if grid[i][m] * grid[i][m + 1] == 0:
                        m += 1
                        while grid[i][m] == 0:
                            m += 1
                        count += n - m
                        #print(n - m)
                        break

                    elif grid[i][m] * grid[i][m + 1] < 0:
                        count += n - m - 1
                        #print(n - m - 1)
                        break

                    else:
                        if grid[i][m] > 0:
                            l = m + 1
                        else:
                            r = m - 1

        return count
