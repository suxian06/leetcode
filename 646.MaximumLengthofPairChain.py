class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        L = len(pairs)
        if L < 2:
            return L

        dp = [1]*L
        maxLength = 1
        pairs.sort()
        for i in range(1,L):
            for j in range(i):
                if pairs[i][0] > pairs[j][1]:
                    dp[i] = max(dp[j] + 1, dp[i])
            if maxLength < dp[i]:
                maxLength = dp[i]
        return maxLength
