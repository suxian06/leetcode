class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        pre_table = {}
        cur_table = {}

        for c in A[0]:
            if c not in pre_table:
                pre_table[c] = 1
            else:
                pre_table[c] += 1

        for s in A[1:]:
            for c in s:
                if c not in cur_table:
                    cur_table[c] = 1
                else:
                    cur_table[c] += 1

            toRemove = set(pre_table.keys()).difference(cur_table.keys())
            for k in toRemove:
                pre_table.pop(k)

            toQuant = set(pre_table.keys()).intersection(cur_table.keys())
            for k in toQuant:
                pre_table[k] = min(pre_table[k],cur_table[k])

            cur_table = {}

        res = []
        for k in pre_table.keys():
            v = pre_table[k]
            while v > 0:
                res.append(k)
                v -= 1
        return res
