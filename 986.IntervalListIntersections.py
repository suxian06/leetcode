# Runtime: 164 ms, faster than 24.01% of Python3 online submissions for Interval List Intersections.
# Memory Usage: 14.6 MB, less than 6.06% of Python3 online submissions for Interval List Intersections.
class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:

        if not A or not B:
            return []

        if A[0][0] > B[0][0]:
            A ,B = B, A
        i , mark, ans = 0, 0, []
        while i < len(A):
            for j in range(mark,len(B)):
                if B[j][0] <= A[i][1]:
                    potential = [max(A[i][0],B[j][0]),min(A[i][1],B[j][1])]
                    if potential[0] <= potential[1]: ans.append(potential)
                else:
                    mark = max(0,j - 1)
                    break
            i += 1
        return ans
