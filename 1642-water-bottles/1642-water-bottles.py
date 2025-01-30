class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        left_over = 0
        res = numBottles
        while numBottles >= numExchange:
            left_over = numBottles%numExchange
            res += numBottles//numExchange
            numBottles//=numExchange
            numBottles+=left_over
            
        return res
