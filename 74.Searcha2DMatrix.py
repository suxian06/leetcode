# Runtime: 64 ms, faster than 95.54% of Python3 online submissions for Search a 2D Matrix.
# Memory Usage: 14.9 MB, less than 5.88% of Python3 online submissions for Search a 2D Matrix.

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        if not matrix or not matrix[0]:
            return False

        n,m = len(matrix), len(matrix[0])
        r = 0
        while target > matrix[r][-1] and r < n - 1:
            r += 1

        c = 0
        while target > matrix[r][c] and c < m - 1:
            c += 1

        return matrix[r][c] == target
