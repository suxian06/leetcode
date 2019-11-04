# Runtime: 80 ms, faster than 48.08% of Python3 online submissions for DI String Match.
# Memory Usage: 14.8 MB, less than 5.00% of Python3 online submissions for DI String Match.
# initially I was considering like this
class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        c = 0
        res = []
        tmp = []
        i = 0
        for s in S:
            if s == "D":
                c += 1
                tmp.append(i)
                i += 1

            elif c == 0:
                res.append(i)
                i += 1
            else:
                tmp.append(i)
                res += tmp[::-1]
                tmp = []
                c = 0
                i += 1
        if c > 0:
            tmp.append(i)
            res += tmp[::-1]
        else:
            res.append(i)
        return res
# Runtime: 76 ms, faster than 73.94% of Python3 online submissions for DI String Match.
# Memory Usage: 14.8 MB, less than 5.00% of Python3 online submissions for DI String Match.
# Then I find some common pattern for the answer
class Solution:
    def diStringMatch(self, S: str) -> List[int]:

        l, r = 0,len(S)
        res = []
        for s in S:
            if s == "D":
                res.append(r)
                r -= 1
            else:
                res.append(l)
                l += 1

        res.append(l)
        return res
