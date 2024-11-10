class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashed = defaultdict(list)
        for item in strs:
            value = ''.join(sorted(item))
            hashed[value].append(item)
        return [ values for values in hashed.values()]