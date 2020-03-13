# Runtime: 144 ms, faster than 83.96% of Python3 online submissions for Lemonade Change.
# Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Lemonade Change.

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change = {5:0,
                  10:0,
                  20:0}

        for var in bills:
            if var == 5:
                change[var] += 1

            elif var == 10:
                change[5] -= 1
                change[var] += 1
                if change[5] < 0:
                    return False

            else:
                if change[10] > 0 and change[5] > 0:
                    change[10] -= 1
                    change[5] -= 1
                    change[var] += 1

                elif change[5] > 2:
                    change[5] -= 3
                    change[var] += 1
                else:
                    return False

        return True
