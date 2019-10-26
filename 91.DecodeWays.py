
# DP solution
# Runtime: 40 ms, faster than 64.72% of Python3 online submissions for Decode Ways.
# Memory Usage: 13.8 MB, less than 16.00% of Python3 online submissions for Decode Ways.
class Solution:
    def numDecodings(self, s: str) -> int:

        dp = [0 for i in range(len(s) + 1)]
        dp[0] = 1

        if s[0] == "0":
            return 0

        dp[1] = 1

        for i in range(1,len(s)):
            if int(s[i]) != 0:
                if  10 < int(s[i - 1:i + 1]) < 27:
                    dp[i + 1] = dp[i - 1] + dp[i]
                else:
                    dp[i + 1] = dp[i]

            elif int(s[i]) == 0:
                if int(s[i - 1]) > 2 or int(s[i - 1]) == 0:
                    return 0
                else:
                    dp[i + 1] = dp[i - 1]

        return dp[-1]

# Using recursive call
# Runtime: 40 ms, faster than 64.72% of Python3 online submissions for Decode Ways.

class Solution:
    def numDecodings(self, s: str) -> int:

        def recursive(s):
            c = 0
            if len(s) < 2:
                return int(s!= "0")

            if int(s[0]) > 0:
                c += recursive(s[1:])

            if 9 < int(s[:2]) < 27:
                c += recursive(s[2:])

            return c

        def calling(s):

            if s[0] == "0":
                return 0

            if s[-1] == "0" and int(s[-2]) > 2:
                return 0

            ways = 1
            stack = ""
            for i in range(1,len(s)):
                if len(stack) < 2:
                    stack = s[i - 1]

                if int(s[i - 1: i + 1]) < 27:
                    stack += s[i]

                else:
                    ways *= recursive(stack)
                    stack = ""

            if len(stack) > 1:
                ways *= recursive(stack)
            return ways

        return calling(s)
