class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if set(s) != set(t):
            return False

        if len(s) != len(t):
            return False

        for v in set(s):
            if s.count(v) != t.count(v):
                return False

        return True
        
