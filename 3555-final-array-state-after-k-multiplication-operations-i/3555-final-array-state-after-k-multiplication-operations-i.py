class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        i = 0
        operation_counter = 0
        while True:
            if operation_counter  == k:
                break
            if i == len(nums):
                i = 0
            index = nums.index(min(nums))
            nums[index] = multiplier * nums[index]
            i+=1
            operation_counter+=1
        return nums
            
        