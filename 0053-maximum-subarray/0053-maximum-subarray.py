class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #using kaden's algorithm
        max_value_list = nums[0]
        max_value = nums[0]
        for i in range(1,len(nums)):
            max_value_list = max(max_value_list+nums[i],nums[i])
            max_value = max(max_value,max_value_list)
        return max_value
