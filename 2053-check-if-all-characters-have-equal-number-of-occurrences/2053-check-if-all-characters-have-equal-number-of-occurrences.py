class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        #create a counter for s
        counter_s = Counter(s)
        first_value = counter_s[s[0]]
        for value in counter_s.values():
        #check if there is a defection from the value of the first counter
            if value != first_value:
                return False
        return True