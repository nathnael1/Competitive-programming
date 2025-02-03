class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res = []
        
        #itterating through the list
        for i in range(len(nums)):
            #divide the number it self getting its remainder and value and appending in res
            temp_res = []
            value = nums[i]
            while value > 0:
                remainder = value % 10    
                value//=10
                temp_res.append(remainder)
            temp_res = temp_res[::-1]
            res.extend(temp_res)
        return res