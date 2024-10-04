from itertools import combinations_with_replacement as combinations
class Solution:
    def countVowelStrings(self, n: int) -> int:
        vowels = ["a","e","i","o","u"]
        value = list(combinations(vowels,n))
        return len(value) 
