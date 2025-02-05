class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        #sorting the array
        nums.sort()
        #since the last parts are greater we return the last 3
        #edge case we have to check the last 3 but if it contain 2-ve values first we have to multiply the 
        #first 2 value and then multiply it by the last to get the max_value
        last3 = prod(nums[-3:])
        first3 = nums[0]*nums[1]*nums[-1]
        return max(first3,last3)