# Runtime: 620 ms, faster than 42.42% of Python3 online submissions for Sort Colors.
# Memory Usage: 14.2 MB, less than 100.00% of Python3 online submissions for Sort Colors.

class Solution:
    res = []
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.res = []
        nums = list(range(1,n + 1))

        def c(n,k,path):
            if len(path) == k:
                self.res.append(path)
            for i in range(len(n)):
                c(n[i + 1:],k,path + [n[i]])

        c(nums,k,[])
        return self.res
