class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for items in strs:
            item = ''.join(sorted(items))
            res[item].append(items)
        return [val for item,val in res.items()]