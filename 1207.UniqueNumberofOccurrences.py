class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:

        hash_table = {}
        for v in arr:
            if v not in hash_table:
                hash_table[v] = 1
            else:
                hash_table[v] += 1

        return len(set(hash_table.values())) == len(hash_table.keys())
