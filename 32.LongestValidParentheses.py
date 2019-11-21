# Runtime: 36 ms, faster than 99.48% of Python3 online submissions for Longest Valid Parentheses.
# Memory Usage: 13.5 MB, less than 55.56% of Python3 online submissions for Longest Valid Parentheses.
# stack solution
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        res = 0
        for i,c in enumerate(s):
            if c == "(":
                stack.append(i)
            elif c == ")" and stack:
                stack.pop()
                if stack:
                    res = max(res,i - stack[-1])
                else:
                    stack.append(i)
        return res
# Runtime: 48 ms, faster than 86.21% of Python3 online submissions for Longest Valid Parentheses.
# Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Longest Valid Parentheses.
# dp solution
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        dp = [0 for i in range(len(s))]
        maxLen = 0
        for i in range(1,len(s)):
            if s[i] == ")" and s[i - 1] == "(":
                dp[i] = dp[i - 2] + 2
            elif s[i] == ")" and i - 1 - dp[i - 1] >= 0 and s[i - 1 - dp[i - 1]] == "(":
                dp[i] = dp[i - 1] + 2 + dp[i - 2 - dp[i - 1]]
            if dp[i] > maxLen:
                maxLen = dp[i]
        return maxLen
