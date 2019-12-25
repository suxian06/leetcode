# Runtime: 96 ms, faster than 96.41% of Python3 online submissions for Delete Columns to Make Sorted.
# Memory Usage: 13.7 MB, less than 33.33% of Python3 online submissions for Delete Columns to Make Sorted.

class Solution:
    def minDeletionSize(self, A: List[str]) -> int:

        return sum(1 for v in [*zip(*A)] if list(v) != sorted(v))
