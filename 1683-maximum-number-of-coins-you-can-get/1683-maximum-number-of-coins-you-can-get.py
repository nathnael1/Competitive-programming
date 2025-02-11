class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        #poping the first, second and the third  taking the value of the second
        piles.sort()
        res = 0

        #coins to take
        coins= len(piles)//3
        amount = 0
        while coins != amount:
            piles.pop()
            res += piles.pop()
            amount+=1
        return res