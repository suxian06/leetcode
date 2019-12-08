# Runtime: 348 ms, faster than 74.02% of Python3 online submissions for Word Search.
# Memory Usage: 14.2 MB, less than 74.47% of Python3 online submissions for Word Search.
class Solution:
    ans = False
    def exist(self, board: List[List[str]], word: str) -> bool:

        if not word:
            return False

        def traverse(i, j, word):

            if self.ans:
                return

            if not word:
                self.ans = True
                return

            else:
                axis = [[i - 1,j], [i + 1, j], [i, j - 1], [i, j + 1]]
                for v in axis:
                    if -1 < v[0] < len(board) and -1 < v[1] < len(board[0]) and board[v[0]][v[1]] == word[0]:
                        board[v[0]][v[1]] = ""
                        traverse(v[0], v[1], word[1:])
                        board[v[0]][v[1]] = word[0]

        # initiation
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if not self.ans:
                        board[i][j] = ""
                        traverse(i, j, word[1:])
                        board[i][j] = word[0]

        return self.ans
