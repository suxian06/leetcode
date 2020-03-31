# Runtime: 48 ms, faster than 77.80% of Python3 online submissions for Intersection of Two Arrays II.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Intersection of Two Arrays II.

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        if len(nums2) > len(nums1):
            nums1, nums2 = nums2, nums1

        i, res = 0, []
        for v in nums2:

            while i < len(nums1) and v > nums1[i]:
                i += 1

            if i > len(nums1) - 1:
                break

            if v == nums1[i]:
                res.append(v)
                i += 1

        return res
