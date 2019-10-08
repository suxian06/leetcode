class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        L = len(asteroids)
        #if L == 0:
        #    return asteroids
        i = 1

        while i != L:
            if i == 0:
                i += 1
            prev = asteroids[i - 1] > 0
            stat = asteroids[i] > 0
            if prev == True and stat == False:
                if abs(asteroids[i]) == abs(asteroids[i - 1]):
                    asteroids.pop(i - 1)
                    asteroids.pop(i - 1)
                    i -= 1
                    L = len(asteroids)
                else:
                    asteroids.pop([i - 1, i][abs(asteroids[i - 1]) > abs(asteroids[i])])
                    i -= 1
                    L = len(asteroids)

                if len(asteroids) < 2:
                    return asteroids

            else:
                i += 1
                prev = stat
        return asteroids
