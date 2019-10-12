class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        return " ".join([x for x in s.split(" ") if x != ""][::-1])
        
