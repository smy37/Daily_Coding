import string

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) == 1:
            return True

        def check_lower(w):
            if w in string.ascii_lowercase:
                return True
            else:
                return False

        if check_lower(word[0]):
            for w in word[1:]:
                if not check_lower(w):
                    return False
        else:
            if check_lower(word[1]):
                for w in word[2:]:
                    if not check_lower(w):
                        return False
            else:
                for w in word[2:]:
                    if check_lower(w):
                        return False
        return True