class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashed = {}
        for i in strs:
            sorted_word = ''.join(sorted(i))
            if sorted_word not in hashed:
                hashed[sorted_word] = []
            hashed[sorted_word].append(i)
        return [value for item,value in hashed.items()]
       