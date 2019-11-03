# Runtime: 40 ms, faster than 81.84% of Python3 online submissions for Unique Morse Code Words.
# Memory Usage: 13.8 MB, less than 5.00% of Python3 online submissions for Unique Morse Code Words.

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:

        hash_table = dict(zip([chr(i) for i in range(97,123)],[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]))

        return len(set(["".join(hash_table[x] for x in words[i]) for i in range(len(words)) ]))
