from collections import Counter
class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        #finding total amound of letter
        counter_letter = Counter(s)

        #returning the result
        return int((counter_letter[letter]/len(s)) * 100)