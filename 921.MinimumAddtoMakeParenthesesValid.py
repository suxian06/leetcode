# Runtime: 36 ms, faster than 79.33% of Python3 online submissions for Minimum Add to Make Parentheses Valid.
# Memory Usage: 13.7 MB, less than 8.33% of Python3 online submissions for Minimum Add to Make Parentheses Valid.

class Solution:
    def minAddToMakeValid(self, S: str) -> int:

        while "()" in S:
            S = S.replace("()","")

        return len(S)
