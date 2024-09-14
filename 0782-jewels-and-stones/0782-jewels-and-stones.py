class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        hash = set(jewels)
        counter = 0
        for i in stones:
            if i in hash:
                counter+=1
        return counter