class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #left prefix sum
        res = [1]*(len(nums))
        prefix = 1
        for i in range(len(nums)):
            res[i]*=prefix
            prefix*=nums[i]
        #right prefix sum
        suffix = 1
        for i in range(len(nums)-1,-1,-1):
            res[i]*=suffix
            suffix*=nums[i]
        return res
        