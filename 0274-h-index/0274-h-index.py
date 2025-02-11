class Solution:
    def hIndex(self, citations: List[int]) -> int:
        #sorting the citations
        citations.sort()
        h_index = 0
        for i in range(len(citations)):
            value = min(citations[i],len(citations)-i)
            h_index = max(value,h_index)
        return h_index