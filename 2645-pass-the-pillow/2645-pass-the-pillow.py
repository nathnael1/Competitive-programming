class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        l = 1
        left = True
        while time > 0:
            if l == n:
                left = False
            elif l == 1:
                left = True
            if left:
                l+=1
            if not left:
                l-=1
            time-=1
        return l
             
