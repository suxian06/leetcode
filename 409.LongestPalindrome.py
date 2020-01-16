# Runtime: 32 ms, faster than 50.47% of Python3 online submissions for Longest Palindrome.
# Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Longest Palindrome.
class Solution:
    def longestPalindrome(self, s: str) -> int:
        table = {}
        for v in s:
            if v in table:
                table[v] += 1
            else:
                table[v] = 1
        ans, odd, add = 0, False, False

        for v in table.values():
            if v > 1:
                if v % 2:
                    ans += v - 1
                    odd = True
                else:
                    ans += v
            else:
                add = True
        return ans + 1 if odd or add else ans
