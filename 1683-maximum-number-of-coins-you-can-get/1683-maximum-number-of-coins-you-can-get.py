class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse = True)
        res = 0
        counter = 0
        max_coin = len(piles)/3
        for i in range(1,len(piles),2):
            if counter == max_coin:
                break
            res += piles[i]
            counter+=1
        return res