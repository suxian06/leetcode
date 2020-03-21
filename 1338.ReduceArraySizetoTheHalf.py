# Runtime: 600 ms, faster than 93.29% of Python3 online submissions for Reduce Array Size to The Half.
# Memory Usage: 29.6 MB, less than 100.00% of Python3 online submissions for Reduce Array Size to The Half.
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        hash_table = {}
        for var in arr:
            if var not in hash_table:
                hash_table[var] = 1
            else:
                hash_table[var] += 1
        L = len(arr)
        goal = L // 2

        iterations = sorted(hash_table.values(),reverse = True)

        c = 0
        for var in iterations:
            if L - var > goal:
                L -= var
                c += 1
            else:
                return c + 1
