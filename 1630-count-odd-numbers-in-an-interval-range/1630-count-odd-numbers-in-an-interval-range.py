class Solution:
    def countOdds(self, low: int, high: int) -> int:
        counter = 0
        if high % 2 == 0 and low % 2 == 0:
            return int((high-low)/2)
        elif high % 2 == 1 and low % 2 == 1:
            return int((high-low)/2 + 1)
        else:
            return int((high-low+1)/2)
        
            