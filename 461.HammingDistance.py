# Runtime: 36 ms, faster than 72.05% of Python3 online submissions for Hamming Distance.
# Memory Usage: 13.8 MB, less than 8.70% of Python3 online submissions for Hamming Distance.

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:

        return bin(x ^ y).count("1")
