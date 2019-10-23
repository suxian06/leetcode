class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0:
            return False
        m, n = len(matrix), len(matrix[0])

        if n == 0:
            return False

        i,j = 0, n - 1
        while j > -1 and i < m:
            if matrix[i][j] > target:
                j -= 1
            elif matrix[i][j] < target:
                i += 1
            elif matrix[i][j] == target:
                return True


        return False
