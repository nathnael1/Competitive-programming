class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #using kaden's algorithm
        res = float('-inf')
        sub_array = 0
        for i in range(len(nums)):
            sub_array+= nums[i]
            if sub_array < nums[i]:
                res = max(res,nums[i])
                sub_array = nums[i]
            else:
                res = max(res,sub_array)
            print(res)
        return res