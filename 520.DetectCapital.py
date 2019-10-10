class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if word.upper() == word:
            return True
        elif word.lower() == word:
            return True
        elif word[0].upper() + word[1:] == word[0] + word[1:].lower():
            return True

        return False
        
