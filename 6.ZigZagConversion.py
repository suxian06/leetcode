# Runtime: 48 ms, faster than 99.56% of Python3 online submissions for ZigZag Conversion.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for ZigZag Conversion.

class Solution:
    def convert(self, s: str, numRows: int) -> str:

        L = len(s)
        if numRows == 1 or numRows > L:
            return s

        dist = numRows + numRows - 2
        res = ""

        maxDist = int(L / dist) * dist

        if maxDist == 0:
            pos = dist - L + 1
            res += s[:pos]
            i, j = pos, L - 1

            while i < j:
                res += s[i] + s[j]
                i += 1
                j -= 1

            if i == j:
                res += s[i]
            return res

        i , j = 0, 0
        for i in range(numRows):
            tmp = s[i]
            for d in range(dist, L + 1, dist):

                if 0 < i < numRows - 1:
                    tmp += s[i + d - j]

                if i + d < L:
                    tmp += s[i + d]

                if d == maxDist:
                    if dist - j > 0 and j != 0 :
                        if i + d + dist - j < L:
                            tmp += s[i + d + dist - j]

            j += 2
            res += tmp

        return res
