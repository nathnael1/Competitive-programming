from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        #constructing a counter
        counter = Counter(s)
        
        #changing the counter to list format
        res = list([element,freq] for element,freq in counter.items())
        res.sort(key = lambda x: x[1],reverse = True)
        res = [element*freq for element,freq in res]
        return "".join(res)
        