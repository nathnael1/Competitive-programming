class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        #we have to create res array with same length 
        res = [""] * len(s)

        for index,value in enumerate(indices):
            #inserting the element to res with given indices
            res[value] = s[index]
        return "".join(res)