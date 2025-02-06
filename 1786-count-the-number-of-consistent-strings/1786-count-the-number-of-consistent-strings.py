class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        #changing str to set
        allowed_set = set(allowed)
        res = 0

        #changin each word to set and comparing if the string is a subset or not
        for word in words:
            word_set = set(word)
            if word_set <= allowed_set:
                res+=1
        return res 