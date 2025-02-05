class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        res = []
        #create a set for first,second, and third row
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")
        #go through the words for each word check if it is subset and append it to res
        for word in words:
            lower_word = set(word.lower())
            if lower_word <= row1 or lower_word <= row2 or lower_word <= row3:
                res.append(word)
        return res