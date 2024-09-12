class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)
        counter = 0
        for word in words:
            word = set(word)
            result = word - allowed
            if len(result) == 0:
                counter+=1
        return counter