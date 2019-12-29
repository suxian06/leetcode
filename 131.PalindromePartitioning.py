# Runtime: 80 ms, faster than 77.80% of Python3 online submissions for Palindrome Partitioning.
# Memory Usage: 13 MB, less than 100.00% of Python3 online submissions for Palindrome Partitioning.

class Solution:
    ans = []
    def partition(self, s: str) -> List[List[str]]:

        self.ans = []

        def palin(s,p):

            if not s:
                self.ans.append(p)
            else:
                L = len(s)
                for i in range(1, L + 1):
                    if s[:i] == s[:i][::-1]:
                        palin(s[i:], p + [s[:i]])

        palin(s,[])
        return self.ans
