# Runtime: 20 ms, faster than 99.33% of Python online submissions for Valid Anagram.
# Memory Usage: 12.5 MB, less than 100.00% of Python online submissions for Valid Anagram.
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
