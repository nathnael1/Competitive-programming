class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        #poping the first, second and the third  taking the value of the second
        piles.sort()
        res = 0
        while piles:
            piles.pop()
            res += piles.pop()
            piles.pop(0)
        return res