# Runtime: 56 ms, faster than 94.20% of Python3 online submissions for Combination Sum.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Combination Sum.
# recursive solution
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def traverse(candidates,target,s,path,res):
            if s < target:
                for i in range(len(candidates)):
                    if candidates[i] + s <= target:
                        traverse(candidates[i:],target,s + candidates[i],path + [candidates[i]],res)
            elif s == target:
                res.append(path)
        traverse(candidates,target,0,[],res)
        return res
