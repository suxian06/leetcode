# Runtime: 272 ms, faster than 87.48% of Python3 online submissions for 4Sum II.
# Memory Usage: 60 MB, less than 8.33% of Python3 online submissions for 4Sum II.

class Solution:

    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        from collections import Counter
        sAB = Counter(a + b for a in A for b in B)
        sCD = Counter(c + d for c in C for d in D)

        count = 0
        for x in sAB:
            if -x in sCD:
                count += 1*sAB.get(x)*sCD.get(-x)
        return count
