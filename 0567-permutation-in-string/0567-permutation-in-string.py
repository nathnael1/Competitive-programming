class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #checking counter for every slice
        n = len(s1)
        p = 0
        while p < len(s2)-n+1:
            if Counter(s2[p:p+n]) == Counter(s1):
                return True
            p+=1
        return False