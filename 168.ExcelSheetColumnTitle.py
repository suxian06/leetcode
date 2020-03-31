# Runtime: 24 ms, faster than 90.93% of Python3 online submissions for Excel Sheet Column Title.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Excel Sheet Column Title.
class Solution:
    def convertToTitle(self, n: int) -> str:
        table = dict(zip(range(1,27),"ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
        s, tail = 27, ""

        if n < 27:
            return table[n]

        while s > 26:
            s,n = divmod(n,26)
            if not n:
                tail = "Z" + tail
                s -= 1
            else:
                tail = table[n] + tail
            n = s

        if not s:
            return tail
        return table[s] + tail
