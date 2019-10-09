class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        table = {}
        res = []
        L = len(nums2)

        for i in range(len(nums2)):
            j = i + 1

            while j < L:
                if nums2[i] < nums2[j]:
                    table[nums2[i]] = nums2[j]
                    break
                else:
                    j += 1

        for val in nums1:
            if val in table:
                res.append(table[val])
            else:
                res.append(-1)

        return res
