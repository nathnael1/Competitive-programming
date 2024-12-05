class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        order = len(nums) * [0]
        counter = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] > nums[j]:
                    counter +=1
                    order[i] = counter
            counter = 0
        return order