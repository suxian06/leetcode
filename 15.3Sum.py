class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        L = len(nums)

        for i in range(L-2):
            if i == 0 or nums[i] > nums[i-1]:
                left = i+1
                right = L-1
                while left < right:

                    if -nums[i] == nums[left] + nums[right]:
                        res.append([nums[left],nums[i],nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -=1

                    elif -nums[i] < nums[left] + nums[right]:
                        while left < right:
                            right -= 1
                            if nums[right] < nums[right + 1]:
                                break

                    else:
                        while left < right:
                            left += 1
                            if nums[left] > nums[left - 1]:
                                break
        return res
