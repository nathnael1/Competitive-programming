class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        count = Counter(s)
        checker = count[s[0]]
        for key,value in count.items():
            if value!=checker:
                return False
        return True