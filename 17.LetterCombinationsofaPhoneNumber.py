# Runtime: 28 ms, faster than 96.97% of Python3 online submissions for Letter Combinations of a Phone Number.
# Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Letter Combinations of a Phone Number.
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        table = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        res = [""]
        for v in digits:
            res = [x + d for x in res for d in table[v]]
        return res
