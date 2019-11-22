# Runtime: 24 ms, faster than 97.98% of Python3 online submissions for Decode Ways.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Decode Ways.

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        T = [[1],[1,1]]
        for i in range(2,numRows):
            r = [1]*(i + 1)
            for j in range(1,i):
                r[j] = T[i - 1][j - 1] + T[i - 1][j]
            T.append(r)

        return T[:numRows]
