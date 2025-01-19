class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashed = {}
        for i in range(len(nums)):      
            diff = target - nums[i]     
            if nums[i] not in hashed:
                hashed[diff] = i 
            else:
                return [i,hashed[nums[i]]]
