# not space efficient.

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row_stack = set()
        col_stack = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    col_stack.add(j)
                    row_stack.add(i)


        for r in row_stack:
            matrix[r] = [0 for i in range(len(matrix[r]))]

        for c in col_stack:
            for i in range(len(matrix)):
                matrix[i][c] = 0
