class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res = ""
        l = 0
        for i in range(len(s)):
            if l < len(spaces) and i == spaces[l]:
                res += " "
                res += s[i]
                l+=1
                continue
            res+=s[i]
        return res