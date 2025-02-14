from collections import Counter,defaultdict
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        #handling edge case
        if len(p) > len(s):
            return []
        
        #2 pointer technique
        #counting occurance of p
        p_count = Counter(p)
        window_size = defaultdict(int)
        for i in range(len(p)):
            window_size[s[i]]+=1
        l = 0
        if window_size ==  p_count:
            res.append(l)
        for r in range(len(p),len(s)):
            window_size[s[l]]-=1
            if window_size[s[l]] == 0:
                window_size.pop(s[l])
            window_size[s[r]]+=1
            l+=1
            if window_size ==  p_count:
                res.append(l)
            
        return res
