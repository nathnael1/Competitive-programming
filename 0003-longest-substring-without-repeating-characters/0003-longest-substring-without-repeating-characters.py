class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #using 2 pointer 

        l = 0
        value = set()
        max_width = 0
        for r in range(len(s)):
            while s[r]  in value:
                value.discard(s[l])
                l+=1
            value.add(s[r])
            max_width = max(max_width,r-l+1)
        return max_width