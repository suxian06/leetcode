# Runtime: 36 ms, faster than 96.72% of Python3 online submissions for Relative Sort Array.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Relative Sort Array.
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        inarr, outarr = [], []
        for v in arr1:
            if v in arr2:
                inarr.append(v)
            else:
                outarr.append(v)

        def index_func(val):
            return arr2.index(val)

        return sorted(inarr,key = index_func) + sorted(outarr)
