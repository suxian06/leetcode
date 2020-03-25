# Runtime: 104 ms, faster than 97.94% of Python3 online submissions for The K Weakest Rows in a Matrix.
# Memory Usage: 13.1 MB, less than 100.00% of Python3 online submissions for The K Weakest Rows in a Matrix.

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:

        ans = sorted([sum(mat[i]),i] for i in range(len(mat)))
        return [ x[1] for x in ans[:k]]
        
