class Solution:
    def partitionLabels(self, S: str) -> List[int]:

        pointEnd = {}
        pointStart = {}

        for k in S:
            pointStart[k] = S.find(k)
            pointEnd[k] = S.rfind(k)

        res = [0]
        pointStart = list(pointStart.values())
        pointEnd = list(pointEnd.values())
        for i in range(1,len(pointEnd)):
            if all([ x <pointStart[i] for x in pointEnd[:i]]):
                res.append(pointStart[i])

        res.append(len(S))
        out = []
        for i in range(1,len(res)):
            out.append(res[i] - res[i - 1])

        return out
