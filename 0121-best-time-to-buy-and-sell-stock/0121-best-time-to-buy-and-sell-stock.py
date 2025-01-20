class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum_price = prices[0]
        maximum_price = 0
        for i in range(1,len(prices)):
            if prices[i] < minimum_price:
                minimum_price = prices[i]
            maximum_price = max(maximum_price,prices[i]-minimum_price)
        return maximum_price