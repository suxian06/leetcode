# 112 ms
# 13.9 MB

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        from collections import Counter

        for i in range(9):
            newSet = set()
            for j in range(9):
                if board[i][j] in newSet and board[i][j] != ".":
                    return False
                else:
                    newSet.add(board[i][j])
            newSet = set()
            for k in range(9):
                if board[k][i] in newSet and board[k][i] != ".":
                    return False
                else:
                    newSet.add(board[k][i])

        for i in range(0,9,3):

            j = 0
            newSet = set()
            while j < 9:
                for k in range(i, i + 3):
                    if board[j][k] in newSet and board[j][k] != ".":
                        return False
                    else:
                        newSet.add(board[j][k])

                j += 1
                if j % 3 == 0:
                    newSet = set()

        return True
