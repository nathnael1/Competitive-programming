class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #create a dictionary
        two_sum_dict = {}
        #itterate through nums
        for i in range(len(nums)):
            #if  target-nums not in the dict add in the dict as key and value as index
            diff = target-nums[i]
            #if target-nums exist in dict it means we find the value so return the itterator
            #i and the value of the dict
            if nums[i] not in two_sum_dict:
                two_sum_dict[diff] = i
            else:
                return [i,two_sum_dict[nums[i]]]
