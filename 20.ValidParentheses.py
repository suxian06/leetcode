class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) % 2 != 0:
            return False

        stack = []
        valid = set(["()","[]","{}"])
        l = 0
        while l < len(s):
            if s[l:l+2] in valid:
                s = s[:l] + s[l+2:]
                l -= 1
            else:
                l += 1

        return len(s) == 0

            
