from collections import Counter
class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        #counting  sort
        count_costs = Counter(costs)
        cost_sorted = []
        for i in range(max(costs)+1):
            cost_sorted += [i]*count_costs[i]
        value = 0
        res = 0
        print(cost_sorted)
        # checking if the coin is greater than the cost
        for price in cost_sorted:
            value+=price
            if value > coins:
                break
            res+=1
        return res