class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #checking counter for every slice
        if len(s2) < len(s1):
            return False
        n = len(s1)
        counter_s1 = Counter(s1)
        counter_s2 = defaultdict(int)
        for i in range(n):
            counter_s2[s2[i]]+=1
        #itterating through s2
        l = 0

        for r in range(n,len(s2)):
            print(counter_s2)
            if counter_s1 == counter_s2:
                return True
            
            counter_s2[s2[r]]+=1
            counter_s2[s2[l]]-=1
            if counter_s2[s2[l]] == 0:
                counter_s2.pop(s2[l])
            l+=1
        if counter_s1 == counter_s2:
                return True
        return False