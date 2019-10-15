class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hash_table = {}

        for i in range(len(nums)):

            if nums[i] not in hash_table:
                hash_table[nums[i]] = 1
            else:
                hash_table[nums[i]] += 1

        return sorted(hash_table.keys(),key = hash_table.get,reverse = True)[:k]      
