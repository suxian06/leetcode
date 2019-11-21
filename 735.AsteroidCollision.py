# Runtime: 92 ms, faster than 99.73% of Python3 online submissions for Asteroid Collision.
# Memory Usage: 13.9 MB, less than 25.00% of Python3 online submissions for Asteroid Collision.
# updated using stack
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for v in asteroids:
            if v > 0:
                stack.append(v)

            elif v < 0 and stack:
                if stack[-1] < 0:
                    stack.append(v)
                elif stack[-1] + v == 0:
                    stack.pop()
                else:
                    while stack and stack[-1] > 0 and stack[-1] + v < 0:
                        stack.pop()
                    if stack and stack[-1] + v == 0:
                        stack.pop()
                    elif not stack or stack[-1] < 0:
                        stack.append(v)

            elif not stack:
                stack.append(v)

        return stack
