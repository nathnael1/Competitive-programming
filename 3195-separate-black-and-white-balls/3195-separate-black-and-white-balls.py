class Solution:
    def minimumSteps(self, s: str) -> int:
        #counting number of zeroes after one
        s = list(map(int,s))
        res = 0
        counter_all = Counter(s)
        for r in range(len(s)):
            if s[r] == 1:
                res+=counter_all[0]
            else:
                counter_all[0]-=1
        return res

        