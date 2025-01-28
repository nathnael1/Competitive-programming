class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        max_counter = 1
        l = 0
        seen = set(s[0])
        for i in range(1,len(s)):
            while s[i] in seen:
                seen.remove(s[l])
                l+=1
            seen.add(s[i])
            max_counter = max(max_counter,i-l+1)
        return max_counter