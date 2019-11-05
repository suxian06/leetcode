# Runtime: 112 ms, faster than 84.76% of Python3 online submissions for Group Anagrams.
# Memory Usage: 17.1 MB, less than 35.85% of Python3 online submissions for Group Anagrams.

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        table = {}
        res = []

        for i in range(len(strs)):

            tmp = "".join(sorted(strs[i]))
            if tmp in table.keys():
                table[tmp].append(strs[i])
            else:
                table[tmp] = [strs[i]]

        return table.values()
