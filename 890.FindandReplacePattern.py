# Runtime: 32 ms, faster than 96.96% of Python3 online submissions for Find and Replace Pattern.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Find and Replace Pattern.

class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:

        L = len(pattern)
        c_pattern = [ pattern.count(pattern[i]) for i in range(L) ]
        res = []
        for w in words:
            tmp = dict(zip(w,pattern))
            if all( w.count(w[i]) == c_pattern[i] for i in range(L)):
                if "".join([tmp[x] for x in w]) == pattern:
                    res.append(w)

        return res
