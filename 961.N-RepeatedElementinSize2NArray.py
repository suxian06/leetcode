# Runtime: 220 ms, 99.83%
# Memory Usage: 14.1 MB, 100%

class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:

        if A == []:
            return None
        stack = set()
        for a in A:
            if a not in stack:
                stack.add(a)
            else:
                return a
