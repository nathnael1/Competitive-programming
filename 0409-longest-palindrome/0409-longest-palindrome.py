class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = Counter(s)
        ans = 0
        check = False
        for key,value in counter.items():
            if value %2 == 0:
                ans+=value
            else:
                ans+= value - 1
                check = True
        if check:
            return ans+1

        return ans