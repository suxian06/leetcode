#Runtime: 36 ms, faster than 98.06% of Python3 online submissions for Remove Outermost Parentheses.
#Memory Usage: 13.8 MB, less than 5.56% of Python3 online submissions for Remove Outermost Parentheses.

class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        count = 1
        stack = ""
        for s in S[1:]:

            if s == "(":
                count += 1
                if count > 1:
                    stack += "("

            else:
                count -= 1
                if count != 0:
                    stack += ")"
        return stack
