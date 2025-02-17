class Solution:
    def equalFrequency(self, word: str) -> bool:
        #creating a counter and validator function
        def valid(word_c):
            word_c = Counter(word)
            letters = [chr(i) for i in range(ord('a'), ord('z') + 1)]

            for c in letters:
                if c in word_c:
                    word_c[c]-=1
                    if word_c[c] == 0:
                        word_c.pop(c)
                    set_values = set(word_c.values())
                    if len(set_values) == 1:
                        return True
                    word_c[c]+=1
                else:
                    continue
            return False
        return valid(word)
            