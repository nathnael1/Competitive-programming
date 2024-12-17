class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        i , j = 0 , len(s) - 1
        s= s.upper()
        while i < j:
            if not s[i].isalnum():
                i+=1
                continue
            if not s[j].isalnum():
                j-=1
                continue
            if s[i]== s[j]:
                i+=1
                j-=1
                continue
            return False
        return True

