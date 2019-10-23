class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n):
            for j in range(i,n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(n):
            l, r = 0, n - 1
            while l < r:
                matrix[i][l],matrix[i][r] = matrix[i][r], matrix[i][l]
                l += 1
                r -= 1
