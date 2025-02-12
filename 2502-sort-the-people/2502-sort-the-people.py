class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        #sorting using insertion sort
        
        zipped = list(zip(names,heights))
        zipped.sort(key = lambda x: x[1],reverse = True)
        return [name for name,height in zipped]