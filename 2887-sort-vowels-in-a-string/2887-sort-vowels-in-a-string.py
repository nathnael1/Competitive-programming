class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        vowelsInS = [char for char in s if char in vowels]
        if not vowelsInS:
            return s
        vowelsInS.sort()
        res = []
        vowel_index = 0
        for char in s:
            if char in vowels:
                res.append(vowelsInS[vowel_index])
                vowel_index+=1
                continue
            res.append(char)
        return "".join(res)