class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        L = len(s)
        if L <= 1:
            return s

        pL = 0
        p = ""
        for i in range(L):
            for j in range(L - i, pL , -1):
                if s[i:i + j] == s[i:i + j][::-1]:
                    if len(s[i:i + j]) > pL:
                        p = s[i:i + j]
                        pL = len(p)
        return p
