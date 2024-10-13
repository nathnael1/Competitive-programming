class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        res = {}
        result = []
        container = {}
        min_value = []
        valid = set()
        for word in words:
            temp = {}
            for letter in word:
                res[letter] = res.get(letter,0)+1
                temp[letter] = temp.get(letter, 0) + 1
            for letter,count in temp.items():
                min_value.append([letter,count])
        for let, rep in min_value:
            res[let] = min(res[let],rep)
        for word in words:
            temp = set()
            for letter in word:
                if letter in temp:
                    continue
                container[letter] = container.get(letter,0)+1
                temp.add(letter)
        for items,value in container.items():
            if value == len(words):
                valid.add(items)
        for items,value in res.items():
            if items in valid:
                i  = value
                while i > 0:
                    result.append(items)
                    i-=1
    
        return result

        