# Runtime: 104 ms, faster than 88.88% of Python3 online submissions for Median of Two Sorted Arrays.
# Memory Usage: 13 MB, less than 100.00% of Python3 online submissions for Median of Two Sorted Arrays.

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        m, n = len(nums1), len(nums2)

        if m == 0:
            L, l = divmod(n , 2)
            if l == 0:
                return float((nums2[L - 1] + nums2[L]) / 2)
            else:
                return float(nums2[L])

        if n == 0:
            L, l = divmod(m , 2)
            if l == 0:
                return float((nums1[L - 1] + nums1[L]) / 2)
            else:
                return float(nums1[L])

        L, l = divmod(m + n + 1, 2)
        c = 0
        while nums1 and nums2 and L > 0:
            if nums1[-1] < nums2[-1]:
                c = nums2.pop()
            else:
                c = nums1.pop()
            L -= 1

        if l == 0:
            if L == 0:
                return float(c)
            elif nums1:
                return nums1[-L]
            elif nums2:
                return nums2[-L]

        if nums1 and nums2:
            return float((max(nums1[-1],nums2[-1]) + c) / 2)

        if not nums1:
            if L == 0:
                return float((nums2[-1] + c) / 2)
            else:
                return float((nums2[-L] + nums2[-l - L]) / 2)
        if not nums2:
            if L == 0:
                return float((nums1[-1] + c) / 2)
            else:
                return float((nums1[-L] + nums1[-l - L]) / 2)
