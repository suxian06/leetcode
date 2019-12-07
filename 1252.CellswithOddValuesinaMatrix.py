# Runtime: 52 ms, faster than 38.69% of Python3 online submissions for Cells with Odd Values in a Matrix.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Cells with Odd Values in a Matrix.
class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        empty = [[0 for i in range(m)] for j in range(n)]
        for d in indices:
            empty[d[0]] = [ x + 1 for x in empty[d[0]]]
            for r in range(n):
                empty[r][d[1]] += 1

        return sum((sum(x % 2 == 1 for x in y) for y in empty))
# Runtime: 44 ms, faster than 63.97% of Python3 online submissions for Cells with Odd Values in a Matrix.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Cells with Odd Values in a Matrix.
class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        empty = [[0 for i in range(m)] for j in range(n)]
        newIndice = [*zip(*indices)]
        res = 0
        for r in newIndice[0]:
            empty[r] = [ x + 1 for x in empty[r]]
            #print(empty)
            if empty[r][0] % 2 == 1:
                res += m
            else:
                res -= m
        #print(res)
        for c in newIndice[1]:
            for r in range(n):
                empty[r][c] += 1
                if empty[r][c] % 2:
                    res += 1
                else:
                    res -= 1
        return res
