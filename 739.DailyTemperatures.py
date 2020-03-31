# Runtime: 480 ms, faster than 95.09% of Python3 online submissions for Daily Temperatures.
# Memory Usage: 20.8 MB, less than 5.26% of Python3 online submissions for Daily Temperatures.

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = []
        L = len(T)
        ans = dict(zip(range(L),[0]*L))
        for i in range(1,L):
            if T[i] > T[i - 1]:
                ans[i - 1] = 1
            else:
                stack.append(i - 1)

            if ans[i - 1]:
                while stack and T[stack[-1]] < T[i]:
                    ans[stack[-1]] = i - stack[-1]
                    stack.pop()

        return ans.values()
