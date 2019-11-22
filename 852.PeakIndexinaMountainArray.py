# Runtime: 76 ms, faster than 98.12% of Python3 online submissions for Peak Index in a Mountain Array.
# Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Peak Index in a Mountain Array.

class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        low, high, i = 0, len(A), len(A) // 2
        while not A[i - 1] < A[i] > A[i + 1]:
            if A[i] < A[i - 1]:
                high = i
                i = (low + i) // 2
            elif A[i] > A[i - 1]:
                low = i
                i = (i + high) // 2
        return i
        #return A.index(max(A))
        
# a cleaner version of binary search from leetcode solution
class Solution(object):
    def peakIndexInMountainArray(self, A):
        lo, hi = 0, len(A) - 1
        while lo < hi:
            mi = (lo + hi) // 2
            if A[mi] < A[mi + 1]:
                lo = mi + 1
            else:
                hi = mi
        return lo
