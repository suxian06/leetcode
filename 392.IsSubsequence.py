class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        pos = 0

        for val in s:
            if val not in t[pos:]:
                return False
            else:
                pos += t[pos:].find(val) + 1

        return True
        
