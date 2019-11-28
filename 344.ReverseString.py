# Runtime: 212 ms, faster than 95.12% of Python3 online submissions for Reverse String.
# Memory Usage: 17.1 MB, less than 100.00% of Python3 online submissions for Reverse String.

class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return s
