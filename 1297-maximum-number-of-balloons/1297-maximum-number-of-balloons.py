class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counter = defaultdict(int)
        word = "balon"
        for c in text:
            if c in word:
                counter[c]+=1
        if any(c not in counter for c in word):
            return 0
        return min(counter["a"], counter["b"], counter["l"]//2, counter["o"]//2,counter["n"])