class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counter = Counter('balloon')
        text_count = Counter(text)
        res = float('inf')
        for c in counter:
            res = min(res,text_count[c]//counter[c])
        return res
