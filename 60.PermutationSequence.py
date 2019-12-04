# Runtime: 28 ms, faster than 93.99% of Python3 online submissions for Permutation Sequence.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Permutation Sequence.

class Solution:
    res = ""
    def getPermutation(self, n: int, k: int) -> str:
        from math import factorial
        array = "".join(str(x) for x in list(range(1,n + 1)))

        while n > 0:
            pos = factorial(n - 1)
            c = 0
            while k > pos:
                k -= pos
                c += 1
            n -= 1
            self.res += array[c]
            array = array[:c] + array[c + 1:]

        return self.res
