# Runtime: 20 ms, faster than 99.45% of Python3 online submissions for Excel Sheet Column Number.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Excel Sheet Column Number.

class Solution:
    def titleToNumber(self, s: str) -> int:
        table = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ",range(1,27)))
        L = len(s)
        ans, i = 0, L - 1
        while i > -1:
            ans += 26**(L - 1 - i)*table[s[i]]
            i -= 1
        return ans
