class Solution:
    def firstUniqChar(self, s: str) -> int:
        hash = {}
        res = -1
        for i in s:
            hash[i] = hash.get(i,0)+1
        for index,value in enumerate(s):
            if hash[value] == 1:
                res = index
                break
        return res
        

        