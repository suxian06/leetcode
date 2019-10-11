class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return n

        prevOne = 1
        prevTwo = 2

        while n > 2:

            cur = prevOne + prevTwo
            prevOne = prevTwo
            prevTwo = cur

            n -= 1

        return cur
