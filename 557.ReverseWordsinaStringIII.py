# Runtime: 36 ms, faster than 90.40% of Python3 online submissions for Reverse Words in a String III.
# Memory Usage: 14.5 MB, less than 7.69% of Python3 online submissions for Reverse Words in a String III.

class Solution:
    def reverseWords(self, s: str) -> str:

        return " ".join([ x[::-1] for x in s.split(" ")])
