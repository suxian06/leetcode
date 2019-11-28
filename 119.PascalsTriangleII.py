# Runtime: 24 ms, faster than 98.63% of Python3 online submissions for Decode Ways.
# Memory Usage: 12.9 MB, less than 96.15% of Python3 online submissions for Decode Ways.
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        T = [[1],[1,1]]
        if rowIndex < 2:
            return T[rowIndex]
        prev = T[1]
        for i in range(2, rowIndex + 1):
            r = [1]*(i + 1)
            for j in range(1, i):
                r[j] = prev[j - 1] + prev[j]
            prev = r
        return r
