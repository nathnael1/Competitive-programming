class Solution:
    
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        #creating res variable to store the appended list 
        res = []
        #going through each value to the step left or right by checking weathr it is
        #positive or negative and appending to the result
        for i in range(len(nums)):
            if nums[i] > 0:
                index = (i+nums[i]) % len(nums)
                res.append(nums[index])
            elif nums[i] < 0:
                index = (i - abs(nums[i])) % len(nums)
                res.append(nums[index])
            else:
                res.append(nums[i])
        return res