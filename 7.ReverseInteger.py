# Runtime: 32 ms, faster than 96.37% of Python3 online submissions for Reverse Integer.
# Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Reverse Integer.

class Solution:
    def reverse(self,x):

        numMax, numMin = 2**31, -2**31 - 1

        if x > 0:
            x = str(x)
            while x and x[-1] == "0":
                x = x[:-1]
            if not x:
                return 0
            x = x[::-1]
            if int(x) < numMax:
                return x
            return 0

        else:
            x = str(x)
            while x and x[-1] == "0":
                x = x[:-1]
            if not x:
                return 0
            x = x[::-1][:-1]
            if - int(x) > numMin:
                return "-"+x
            return 0
