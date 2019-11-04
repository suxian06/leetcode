# Runtime: 40 ms, faster than 38.24% of Python3 online submissions for Spiral Matrix.
# Memory Usage: 13.7 MB, less than 8.70% of Python3 online submissions for Spiral Matrix.
# sad
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        if len(matrix) == 0:
            return []
        if len(matrix[0]) == 0:
            return []

        m,n = len(matrix), len(matrix[0])
        res = []
        L = m*n
        i, j, init = 0, 0, 0

        while L > 0:
            while j < n and L > 0:
                res.append(matrix[i][j])
                j += 1
                L -= 1
            j -= 1
            while i < m - 1 and L > 0:
                res.append(matrix[i + 1][j])
                i += 1
                L -= 1
            while j > init and L > 0:
                res.append(matrix[i][j - 1])
                j -= 1
                L -= 1

            init += 1
            while i > init and L > 0:
                res.append(matrix[i - 1][j])
                i -= 1
                L -= 1

            i,j = init, init
            m -= 1
            n -= 1

        return res
