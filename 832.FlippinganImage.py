class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:

        for i in range(len(A)):

            A[i] = [ x ^ 1 for x in A[i][::-1]]

        return A
