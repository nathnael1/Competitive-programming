class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        count = Counter(s)
        count_two = Counter(t)
        for keys,values in count_two.items():
            if keys not in count:
                return keys
            if count_two[keys]!=count[keys]:
                return keys