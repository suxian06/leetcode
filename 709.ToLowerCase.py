class Solution:
    def toLowerCase(self, str: str) -> str:
        return "".join([x if ord(x) > 90 or ord(x) < 65 else chr(ord(x)+32) for x in str])
