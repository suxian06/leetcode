# Runtime: 40 ms, faster than 98.60% of Python3 online submissions for Combination Sum II.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Combination Sum II.

class Solution:
    res = []
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.res = []
        candidates = sorted([x for x in candidates if x <= target])

        def search(candidates,target,s):

            if target == 0:
                self.res.append(s)
                return

            if target < 0:
                return

            init = float("inf")
            i = 0
            while i < len(candidates):
                if candidates[i] != init:
                    if candidates[i] <= target:
                        init = candidates[i]
                        search(candidates[i + 1:],target - candidates[i],s + [candidates[i]])
                    else:
                        break
                i += 1
        search(candidates,target,[])

        return self.res
