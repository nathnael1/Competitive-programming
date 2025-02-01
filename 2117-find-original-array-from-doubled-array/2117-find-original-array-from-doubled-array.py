class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        #if it is not even length we have to return empty array
        if len(changed) % 2 != 0:
            return []
        original = []
        ocurance = Counter(changed)
        changed.sort()
        #we are going to check the number of occurance fo each eiment and if 
        #the double form exist and decrease the counter also handle edge case
        for num in changed:
            if num == 0 and ocurance[num] >= 2:
                ocurance[num]-=2
                original.append(num)
            elif num > 0 and ocurance[num] and ocurance[num*2]:
                ocurance[num]-=1
                ocurance[num*2]-=1
                original.append(num)
            
        return original if len(original) ==  len(changed)//2 else []
        