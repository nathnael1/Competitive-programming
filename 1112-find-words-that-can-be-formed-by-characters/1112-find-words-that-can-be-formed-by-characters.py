from collections import Counter
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        #we have to create counter for both words
        counter_chars = Counter(chars)
        length_unique_chars = 0
        #checking if all value in word is found in chars and decrmenting chars
        for word in words:
            counter_word = Counter(word)
            checker = all(value <= counter_chars[key] for key,value in counter_word.items())
            if checker:
                length_unique_chars += len(word)
        return length_unique_chars
            
