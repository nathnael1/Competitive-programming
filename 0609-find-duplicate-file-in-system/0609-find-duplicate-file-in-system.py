from collections import defaultdict
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        hashed = defaultdict(list)
        for path in paths:
            dirr, *files = path.split()
            for f in files:
                fname, fcont = f.split('(')
                fcont = fcont[:-1]
                hashed[fcont].append(f"{dirr}/{fname}")
        ans = []

        for item,value in hashed.items():
           if len(value) > 1:
                ans.append(value)
        return ans



        
                