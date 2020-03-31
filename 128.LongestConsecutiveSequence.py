# Runtime: 64 ms, faster than 25.38% of Python3 online submissions for Longest Consecutive Sequence.
# Memory Usage: 14.5 MB, less than 100.00% of Python3 online submissions for Longest Consecutive Sequence.
class Solution:
    ans = 0
    def longestConsecutive(self, nums: List[int]) -> int:
        sets, seen = set(nums), dict()

        for v in nums:
            mark = v
            seen[mark] = 1

            while v + 1 in sets and v + 1 not in seen.keys():
                v += 1
            seen[mark] += v - mark

            if v + 1 in seen.keys():
                seen[mark] += seen[v + 1]

            self.ans = max(seen[mark], self.ans)
        return self.ans
