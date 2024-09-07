class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        hash = {}
        counter=0
        for i in words:
            i_ = i[::-1]
            if i in hash or i_ in hash:
                counter+=1
            else:
                hash[i] = 0
        return counter