# Runtime: 36 ms, faster than 77.60% of Python3 online submissions for Split a String in Balanced Strings.
# Memory Usage: 13.7 MB, less than 100.00% of Python3 online submissions for Split a String in Balanced Strings.

class Solution:
    def balancedStringSplit(self, s: str) -> int:

        cR, cL = 0, 0

        #stack = []
        #cur = ""
        count = 0
        for v in s:

            #cur += v
            cR += int(v == "R")
            cL += int(v == "L")

            if cR == cL > 0:
                #stack.append(cur)
                #cur = ""
                count += 1
                cR, cL = 0, 0

        return count
