class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.recursive(0,0,n,"",res)
        return res

    def recursive(self,i,j,n,path,res):

        if len(path) == 2*n:
            res.append(path)
            return None

        if i == j:
            self.recursive(i + 1, j , n, path + "(",res)

        if i < n:
            if i > j :
                self.recursive(i + 1, j , n ,path + "(",res)
                self.recursive(i, j + 1, n ,path + ")",res)
        elif j < n:
            self.recursive(i, j + 1, n ,path + ")",res)

        return None
