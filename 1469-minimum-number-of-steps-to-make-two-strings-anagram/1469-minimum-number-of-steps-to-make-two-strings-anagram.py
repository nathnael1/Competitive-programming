class Solution:
    def minSteps(self, s: str, t: str) -> int:
        operation = 0
        #create a counter for s and t
        counter_s = Counter(s)
        counter_t = Counter(t)
        #increment by one for unique elements in t and take the difference if
        #character t is greater than character s increment the deference
        for key,value in counter_t.items():
            if key in counter_s and value > counter_s[key]:
                operation += abs(value - counter_s[key])
            elif key not in counter_s:
                operation += 1
        return operation