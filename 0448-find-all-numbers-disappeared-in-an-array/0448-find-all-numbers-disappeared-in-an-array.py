class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        #construct the array with length of nums
        table =set(nums)
        res = []
        #finding elements that are not found in table
        for i in range(1,len(nums)+1):
            if i not in table:
                res.append(i)
        
        return res
