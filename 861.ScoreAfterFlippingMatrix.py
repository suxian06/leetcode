# Runtime: 40 ms, faster than 95.58% of Python3 online submissions for Score After Flipping Matrix.
# Memory Usage: 13.7 MB, less than 20.00% of Python3 online submissions for Score After Flipping Matrix.

class Solution:

    def matrixScore(self, A: List[List[int]]) -> int:

        L = len(A)
        for i in range(L):
            if A[i][0] == 0:
                A[i] = [ x ^ 1 for x in A[i]]


        for j in range(1, len(A[0])):
            if sum([A[i][j] for i in range(L)]) < L / 2:
                for i in range(L):
                    A[i][j] ^= 1


        return sum((int("".join(map(str,A[i])),2) for i in range(L)))
