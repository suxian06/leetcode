# Runtime: 408 ms, faster than 82.63% of Python3 online submissions for Minimum Absolute Difference.
# Memory Usage: 28 MB, less than 100.00% of Python3 online submissions for Minimum Absolute Difference.

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        res = []
        min_key = 1000000

        for i in range(1,len(arr)):
            if min_key > arr[i] - arr[i - 1]:
                min_key = arr[i] - arr[i - 1]
                res = [[arr[i - 1],arr[i]]]
            elif min_key == arr[i] - arr[i - 1]:
                res.append([arr[i - 1], arr[i]])
        return res
