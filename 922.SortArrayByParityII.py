# Runtime: 260 ms
# Memory Usage: 16.2 MB
# My initial submission
class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        even = (x for x in A if x % 2 == 0)
        odd = (x for x in A if x % 2 == 1)

        return list(next(even) if i % 2 == 0 else next(odd) for i in range(len(A)))

# A better one using pointer and swap
# Runtime: 244 ms, faster than 82.63% of Python3 online submissions for Sort Array By Parity II.
# Memory Usage: 15.9 MB, less than 8.70% of Python3 online submissions for Sort Array By Parity II.

class Solution(object):
    def sortArrayByParityII(self, A):
        j = 1
        for i in range(0, len(A), 2):
            if A[i] % 2:
                while A[j] % 2:
                    j += 2
                A[i], A[j] = A[j], A[i]
        return A
