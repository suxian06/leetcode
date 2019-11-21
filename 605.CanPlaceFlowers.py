# Runtime: 176 ms, faster than 94.10% of Python3 online submissions for Can Place Flowers.
# Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Can Place Flowers.
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i = 0
        res, c = 0, 0
        flowerbed.insert(0,0)
        while i < len(flowerbed):

            if flowerbed[i] == 1:
                if c != 0:
                    res += (c - 1) // 2
                    c = 0
            else:
                c += 1
            i += 1
        if c != 0:
            res += c // 2

        return res >= n
