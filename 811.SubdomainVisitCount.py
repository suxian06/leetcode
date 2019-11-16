# Runtime: 56 ms, faster than 92.06% of Python3 online submissions for Subdomain Visit Count.
# Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Subdomain Visit Count.
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:

        res = []
        hash_table = {}
        for d in cpdomains:

            count, domain = d.split(" ")
            count = int(count)
            if domain in hash_table.keys():
                hash_table[domain] += count
            else:
                hash_table[domain] = count
            subdomain = [ i for i,x in enumerate(domain) if x == "."]
            for s in subdomain:
                if domain[s + 1:] not in hash_table.keys():
                    hash_table[domain[s + 1:]] = count
                else:
                    hash_table[domain[s + 1:]] += count
        return [ str(hash_table[x]) + " " + x for x in hash_table.keys()]
