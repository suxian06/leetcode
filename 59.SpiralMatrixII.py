# Runtime: 32 ms, faster than 84.53% of Python3 online submissions for Spiral Matrix II.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Spiral Matrix II.

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:

        matrix =[ [0 for i in range(n)] for j in range(n)]
        v, i, j, b = 1, 0, 0, -1
        while n > 0:
            while i < n:
                if not matrix[j][i]:
                    matrix[j][i] = v
                    v += 1
                i += 1

            i -= 1
            while j < n:
                if not matrix[j][i]:
                    matrix[j][i] = v
                    v += 1
                j += 1


            j -= 1
            while i > b:
                if not matrix[j][i]:
                    matrix[j][i] = v
                    v += 1
                i -= 1

            i += 1
            while j > b:
                if not matrix[j][i]:
                    matrix[j][i] = v
                    v += 1
                j -= 1
            j += 1

            b += 1
            i,j = b + 1,b + 1
            n -= 1
        return matrix
# Then I found this StephanPochmann solution ... FeelsBadMan

def generateMatrix(self, n):
    A = [[0] * n for _ in range(n)]
    i, j, di, dj = 0, 0, 0, 1
    for k in xrange(n*n):
        A[i][j] = k + 1
        if A[(i+di)%n][(j+dj)%n]:
            di, dj = dj, -di
        i += di
        j += dj
    return A
