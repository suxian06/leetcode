# Runtime: 616 ms, faster than 14.03% of Python3 online submissions for Palindromic Substrings.
# Memory Usage: 21.2 MB, less than 34.61% of Python3 online submissions for Palindromic Substrings.
# My really slow and redundant DP solution
class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        L = len(s)
        dp = [[False for i in range(L)] for j in range(L)]
        for i in range(L):
            j,k = i, L - 2
            dp[i][i] = True
            dp[i][L - 1] = s[i:L] == s[i:L][::-1]
            if i == 1:
                while i < k:
                    dp[i][k] = s[i:k + 1] == s[i:k + 1][::-1]
                    k -= 1

            else:
                while j < k:
                    dp[j][k] = dp[j - 1][k + 1] or s[j:k + 1] == s[j:k + 1][::-1]
                    k -= 1
            count += sum(dp[i])
        return count
# The kind of standardized solution, test every possible centers of palindrom and spand across centers
class Solution:
    def countSubstrings(self, s: str) -> int:
        L = len(s)
        centers = 2*L - 1
        count = 0
        for c in range(centers):
            l,r = c  // 2, c // 2 + c % 2
            while l >=0 and r < L and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
        return count
