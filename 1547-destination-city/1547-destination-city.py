class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        hash = {}
        checker = set()
        res = []
        ressecond = []
        for cities in paths:
            hash[cities[0]] = cities[1]
    
        for key,value in hash.items():
           res.append(f"{key}")
           res.append(f"{value}")
        for i in res:
            if i in checker:
                ressecond.remove(i)
                continue
            ressecond.append(i)
            checker.add(i)
        for key,value in hash.items():
            if ressecond[0] == key:
                ressecond.remove(ressecond[0])
                break
            elif ressecond[1] == key:
                ressecond.remove(ressecond[1])
                break
        return ressecond[0]

