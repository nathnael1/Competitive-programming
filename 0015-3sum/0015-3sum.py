class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for first in range(len(nums) - 2):
            if first > 0 and nums[first] == nums[first-1]:
                continue
            i , j = first + 1, len(nums) - 1
            while i < j:
                total = nums[first] + nums[i] + nums[j]
                if total == 0:
                    res.append([nums[first],nums[i],nums[j]])
                    while i < j and nums[i] == nums[i+1]:
                        i+=1
                    while i < j and nums[j] == nums[j-1]:
                        j-=1 
                    i+=1
                    j-=1
                elif total > 0:
                    j-=1
                else:
                    i+=1
        return res
