class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        s = list(s)
        prefix_sum = [0]*(len(s))
        for start,end,direction in shifts:
            if direction == 1:
                prefix_sum[start]+=1
                if end < len(prefix_sum) - 1:
                    prefix_sum[end+1]-=1
            else:
                prefix_sum[start]-=1
                if end < len(prefix_sum) - 1:
                    prefix_sum[end+1]+=1
        #constructing prefix_sum
        for i in range(1,len(prefix_sum)):
            prefix_sum[i] += prefix_sum[i-1] 
        
        #changing the prefix_sum
        for i in range(len(s)):
            value = (ord(s[i])+prefix_sum[i] - ord('a')) % 26            
            s[i] = chr(value + ord('a'))
        return "".join(s)
            
