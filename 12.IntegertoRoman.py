# Runtime: 48 ms, faster than 90.73% of Python3 online submissions for Integer to Roman.
# Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Integer to Roman.
class Solution:
    def intToRoman(self, num: int) -> str:
        table = {1:"I",
                 4:"IV",
                 5:"V",
                 9:"IX",
                 10:"X",
                 40:"XL",
                 50:"L",
                 90:"XC",
                 100:"C",
                 400:"CD",
                 500:"D",
                 900:"CM",
                 1000:"M"}
        res = ""
        keys = list(table.keys())

        while num > 0:
            for i in range(len(keys) - 1,-1,-1):
                if num >= keys[i]:
                    res += table[keys[i]]
                    num -= keys[i]
                    break
        return res
