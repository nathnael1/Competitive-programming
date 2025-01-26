class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        for i in range(1,len(nums)):
            if nums[i-1]<nums[i]:
                return min(nums[i-1:])
            elif nums[i] == len(nums) - 1:
                return nums[i]
            