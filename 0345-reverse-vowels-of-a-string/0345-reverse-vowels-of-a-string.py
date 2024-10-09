class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        res = [""] * len(s)
        vowel_container = []
        for i in range(len(s)):
            if s[i] in vowels:
                vowel_container.append(s[i])
                continue
            res[i] = s[i]
        for i in range(len(res)):
            if res[i] == "":
                res[i] = vowel_container.pop()
        return "".join(res)
        