class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        #greddy approach
        costs.sort()
        res  =0
        value = 0
        #checking if the coin is greater than the cost
        for price in costs:
            value+=price
            if value > coins:
                break
            res+=1
        return res