class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        A_trans = [[None for i in range(len(A))] for j in range(len(A[0]))]
        for i in range(len(A[0])):
            A_trans[i] = [A[j][i] for j in range(len(A))]

        return A_trans
            
