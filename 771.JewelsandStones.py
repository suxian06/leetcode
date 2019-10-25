# Runtime: 36 ms, faster than 76.56% of Python3 online submissions for Jewels and Stones.
# Memory Usage: 13.9 MB, less than 5.39% of Python3 online submissions for Jewels and Stones.
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:

        count = 0
        J = set(J)
        for stone in S:
            if stone in J:
                count += 1

        return count
