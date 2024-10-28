class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum = prices[0]
        profit = 0
        for i in range(len(prices)):
            if prices[i] < minimum:
                minimum = prices[i]
            profit = max(profit, prices[i] - minimum)
        return profit
