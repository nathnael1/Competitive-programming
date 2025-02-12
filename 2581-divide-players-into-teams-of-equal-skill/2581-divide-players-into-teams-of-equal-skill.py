class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        #target value per pair
        target = sum(skill)//(len(skill)/2)
        
        #sorting the array using 2 pointer
        skill.sort()
        l = 0
        r = len(skill) - 1
        res = []
        chemistry = 0
        while l < r:
            if skill[l] + skill[r] == target:
                res.append((skill[l],skill[r]))
            else:
                return -1
            l+=1
            r-=1
        for num in res:
            chemistry += num[0] * num[1]
        return chemistry