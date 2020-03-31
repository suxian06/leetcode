class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        a, b = 1, 0
        for v in str(n):
            a *= int(v)
            b += int(v)
        return a - b
