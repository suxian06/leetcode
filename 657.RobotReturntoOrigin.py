# Runtime: 32 ms, faster than 99.32% of Python3 online submissions for Robot Return to Origin.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Robot Return to Origin.
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        return moves.count("U") == moves.count("D") and moves.count("L") == moves.count("R")
