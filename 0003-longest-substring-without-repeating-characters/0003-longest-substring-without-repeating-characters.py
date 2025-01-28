class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_counter = 0
        for i in range(len(s)):
            counter = 0
            seen = set()
            seen.add(s[i])
            counter+=1
            for j in range(i+1,len(s)):
                if s[j] not in seen:
                    seen.add(s[j])
                    counter+=1
                else:
                    break
            max_counter = max(max_counter,counter)
        return max_counter
        