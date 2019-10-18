class Solution:
    def countBits(self, num: int) -> List[int]:

        res = [0,1]

        for i in range(num):

            if 2**i < num:
                res += [x + 1 for x in res]

            else:
                break

        return res[:num + 1]
