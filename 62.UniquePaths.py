# recursion (timeLimt not allowed)
# recursion divide and conquer
# slow
def path(m,n,p,res):

        if m == n == 1:
            if p not in res:
                res.append(p)
        if m > 0:
            path(m - 1, n, p + [(m,n)],res)
        if n > 0:
            path(m, n - 1, p + [(m,n)],res)

        return None

# 2D dynamic programming
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [ [1 for i in range(n)] for j in range(m)]
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]

# 1D
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        dp = [ 1 for i in range(n)]
        for i in range(1,m):
            for j in range(1,n):
                dp[j] += dp[j - 1]

        return dp[-1]
