class Solution:
    def fib(self, N: int) -> int:
        prevTwo = 0
        prevOne = 1

        if N == 0:
            return prevTwo
        if N == 1:
            return prevOne

        else:
            for i in range(2,N + 1):
                prevOne, prevTwo = prevOne + prevTwo, prevOne

        return prevOne
