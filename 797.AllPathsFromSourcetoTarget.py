# Runtime: 104 ms, faster than 90.16% of Python3 online submissions for All Paths From Source to Target.
# Memory Usage: 14.1 MB, less than 100.00% of Python3 online submissions for All Paths From Source to Target.
class Solution:
    res = []
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.res = []
        def run(step,path,target):

            for v in step:
                if v == target:
                    self.res.append(path + [v])
                else:
                    run(graph[v],path + [v],target)
        run(graph[0],[0],len(graph) - 1)
        return self.res
