class Solution:
    def numTilePossibilities(self, tiles: str) -> int:

        res = set()
        def backtracking(tiles,permut):

            if permut not in res:
                if permut != "":
                    res.add(permut)

            for j in range(len(tiles)):
                backtracking(tiles[:j] + tiles[j + 1:],permut + tiles[j])

        backtracking(tiles,"")


        return len(res)
