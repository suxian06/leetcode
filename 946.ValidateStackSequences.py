# Runtime: 84 ms, faster than 76.78% of Python3 online submissions for Validate Stack Sequences.
# Memory Usage: 14 MB, less than 20.00% of Python3 online submissions for Validate Stack Sequences.

class Solution:
    def validateStackSequences(self, pushed, popped) -> bool:

        stack = []
        i,j = 0, 0
        while j < len(popped):
            while not stack or popped[j] != stack[-1]:
                if i < len(pushed):
                    stack.append(pushed[i])
                    i += 1
                else:
                    return False

            if popped[j] == stack[-1]:
                stack.pop()
                j += 1
            else:
                return False
        return True
