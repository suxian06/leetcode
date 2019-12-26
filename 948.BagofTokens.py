# Runtime: 52 ms, faster than 88.52% of Python3 online submissions for Bag of Tokens.
# Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Bag of Tokens.
class Solution:
    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
        point = 0
        tokens.sort()
        while tokens:
            if P >= tokens[0]:
                P -= tokens[0]
                tokens.pop(0)
                point += 1

            elif point > 0 and len(tokens) > 1:
                P += tokens[-1]
                tokens.pop()
                point -= 1

            else:
                break
        return point
