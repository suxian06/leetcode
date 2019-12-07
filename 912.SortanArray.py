# use merge sort
# Runtime: 456 ms, faster than 12.03% of Python3 online submissions for Sort an Array.
# Memory Usage: 19.3 MB, less than 92.86% of Python3 online submissions for Sort an Array.
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def merge(a,b):
            res = []
            while a and b:
                if a[0] > b[0]:
                    res.append(b.pop(0))
                else:
                    res.append(a.pop(0))
            if a:
                res += a
            else:
                res += b
            return res

        def mergeSort(nums):
            m = len(nums) // 2
            if m > 0:
                return merge(mergeSort(nums[:m]),mergeSort(nums[m:]))

            else:
                return nums

        return mergeSort(nums)

# use quick sort
# Runtime: 248 ms, faster than 74.78% of Python3 online submissions for Sort an Array.
# Memory Usage: 19.5 MB, less than 85.71% of Python3 online submissions for Sort an Array.
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def partition(nums):
            if len(nums) > 1:
                m = nums[-1]
                a,b,c = [],[],[]
                for v in nums:
                    if v > m:
                        a.append(v)
                    elif v < m:
                        b.append(v)
                    else:
                        c.append(v)
                return partition(b) + c + partition(a)
            else:
                return nums
        return partition(nums)
