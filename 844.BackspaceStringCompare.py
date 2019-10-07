class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:

        rS = ""
        rT = ""

        for val in S:
            if val != "#":
                rS += val
            elif rS:
                rS = rS[:-1]

        for val in T:
            if val != "#":
                rT += val
            elif rT:
                rT = rT[:-1]

        return rS == rT
