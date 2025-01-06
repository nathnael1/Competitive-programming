class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_number = 0
        for sentence in sentences:
            count = len(sentence.split())
            max_number = max(count,max_number)
        return max_number