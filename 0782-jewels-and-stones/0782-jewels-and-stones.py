class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        hashed = Counter(jewels)
        counter = 0
        for i in stones:
            counter+=hashed[i]
        return counter