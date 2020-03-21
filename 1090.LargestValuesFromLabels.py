# Runtime: 140 ms, faster than 90.07% of Python3 online submissions for Largest Values From Labels.
# Memory Usage: 17.5 MB, less than 100.00% of Python3 online submissions for Largest Values From Labels.

class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], num_wanted: int, use_limit: int) -> int:

        dat = sorted(zip(values,labels),reverse = True)
        ans, cur, labels_collector = 0, 0, {}

        for pair in dat:
            if pair[1] not in labels_collector.keys():
                labels_collector[pair[1]] = 1
                ans += pair[0]
                cur += 1

            elif labels_collector[pair[1]] < use_limit:
                labels_collector[pair[1]] += 1
                ans += pair[0]
                cur += 1

            if cur == num_wanted:
                return ans

        return ans
