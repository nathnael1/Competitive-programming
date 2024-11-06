class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        hashed = set(jewels)
        counter = 0
        for stone in stones:
            if stone in hashed:
                counter+=1
        return counter