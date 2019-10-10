class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        L = min([len(x) for x in strs])

        c = ""
        for i in range(L):
            if len(set([x[i] for x in strs])) == 1:
                c += x[i]
            else:
                return c

        return c
