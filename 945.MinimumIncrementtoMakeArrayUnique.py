# Runtime: 328 ms, faster than 91.23% of Python3 online submissions for Minimum Increment to Make Array Unique.
# Memory Usage: 17.9 MB, less than 50.00% of Python3 online submissions for Minimum Increment to Make Array Unique.

class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:

        if not A:
            return 0
        A.sort()
        c = 0

        cur = A[0]
        for i in range(1,len(A)):
            if A[i] <= cur:
                c += cur - A[i] + 1
                A[i] += cur - A[i] + 1
                cur = A[i]
            elif A[i] > cur:
                cur = A[i]
        return c
