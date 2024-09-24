class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        negative = []
        positive = []
        pindex = 0
        nindex = 0
        for i in nums:
            if i >  0:
                positive.append(i)
            else:
                negative.append(i)
        res = [] 
        p =  True
        while nindex < len(positive):
            if p:
                res.append(positive[pindex])
                pindex+=1
                p = False
            else:
                res.append(negative[nindex])
                nindex+=1
                p = True
        return res

            