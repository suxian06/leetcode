class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        L = 0
        sub = ""
                
        if len(s) <= L:
            return L

        if not sub:

            for i in range(len(s)):
                if s[i] not in sub:
                    sub += s[i]

                else:
                    L = len(sub)
                    s = s[1:]
                    break

            if sub == s and len(sub) > L :
                return len(s)

        while s:

            if len(s) < L:
                return L

            eva = s[0:L + 1]
            if len(set(eva)) > L and len(set(eva)) == len(eva):
                L = len(set(eva))
                sub = eva

            else:
                s = s[1:]

        return L
