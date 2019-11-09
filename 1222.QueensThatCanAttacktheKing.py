# Runtime: 40 ms, faster than 98.16% of Python3 online submissions for Queens That Can Attack the King.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Queens That Can Attack the King.

class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:

        res = []
        diags = [[king[0] + 1,king[1] + 1],[king[0] - 1,king[1] - 1]]
        for diag,i in zip(diags,[1,-1]):
            while -1 < diag[0] < 8 and -1 < diag[1] < 8:
                if diag in queens:
                    res.append(diag)
                    break
                else:
                    diag[0] += i
                    diag[1] += i

        diags = [[king[0] - 1,king[1] + 1],[king[0] + 1,king[1] - 1]]
        for diag,i in zip(diags,[1,-1]):
            while -1 < diag[0] < 8 and -1 < diag[1] < 8:
                if diag in queens:
                    res.append(diag)
                    break
                else:
                    diag[0] -= i
                    diag[1] += i

        y_axis = [x[1] - king[1] for x in queens if x[0] == king[0]]
        if y_axis:
            y_axis_up = [x for x in y_axis if x > 0]
            if y_axis_up:
                res.append([king[0], king[1] + min(y_axis_up)])
            y_axis_down = [x for x in y_axis if x < 0]
            if y_axis_down:
                res.append([king[0], king[1] + max(y_axis_down)])
        x_axis = [x[0] - king[0] for x in queens if x[1] == king[1]]

        if x_axis:
            x_axis_up = [x for x in x_axis if x > 0]

            if x_axis_up:
                res.append([king[0] + min(x_axis_up),king[1]])
            x_axis_down = [x for x in x_axis if x < 0]

            if x_axis_down:
                res.append([king[0] + max(x_axis_down),king[1]])

        return res
