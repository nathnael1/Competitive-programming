class Solution:
    def minSteps(self, s: str, t: str) -> int:
        operation = 0
        #create a counter for s and t
        counter_s = Counter(s)
        counter_t = Counter(t)

        for key,value in counter_t.items():
            if value > counter_s[key]:
                operation += abs(value - counter_s[key])

        return operation