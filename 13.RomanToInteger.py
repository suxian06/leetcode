class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s[::-1]
        table = {"I":1, "V":5, "X":10, "L": 50, "C": 100, "D": 500, "M": 1000}

        num = table[s[0]]
        val = table[s[0]]
        for c in s[1:]:
            t = table[c]
            if t < val:
                num -= t
            else:
                num += t
            val = t

        return num
