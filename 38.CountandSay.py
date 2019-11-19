# Runtime: 28 ms, faster than 98.90% of Python3 online submissions for Count and Say.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Count and Say.
class Solution:
    def countAndSay(self, n: int) -> str:
        c = "1"
        i = 1
        res = ""
        while i < n:
            count = 1
            prev = c[0]
            for v in c[1:]:
                if v == prev:
                    count += 1
                else:
                    res += str(count) + str(prev)
                    prev = v
                    count = 1
            res += str(count) + str(prev)
            c = res
            res = ""
            i += 1
        return c
